from typing import Any, Type, Sequence
from inspect import iscoroutinefunction

from sqlalchemy import Column, INT, VARCHAR, DECIMAL, ForeignKey, BOOLEAN, \
    create_engine, select, Row, RowMapping
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True)

    engine = create_engine('postgresql://belbank:belbank@localhost:5432/bank')
    session = sessionmaker(bind=engine)

    async_engine = create_async_engine('postgresql+asyncpg://belbank:belbank@localhost:5432/bank')
    async_session = async_sessionmaker(bind=async_engine)

    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with Base.session() as session:
                return func(*args, **kwargs, session=session)

        async def async_wrapper(*args, **kwargs):
            async with Base.async_session() as session:
                return await func(*args, **kwargs, session=session)

        return async_wrapper if iscoroutinefunction(func) else wrapper

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    @create_session
    async def save(self, session: AsyncSession = None) -> None:
        session.add(self)
        await session.commit()
        await session.refresh(self)

    @classmethod
    @create_session
    async def get(cls, pk: Any, session: AsyncSession = None) -> Type["Base"]:
        return await session.get(cls, pk)

    @classmethod
    @create_session
    async def select(
            cls,
            *args,
            order_by: Any = 'id',
            limit: int = None,
            offset: int = None,
            session: AsyncSession = None
    ) -> Sequence[Row | RowMapping | Any]:
        objs = await session.scalars(
            select(cls)
            .order_by(order_by)
            .limit(limit)
            .offset(offset)
            .filter(*args)
        )
        return objs.all()

    @create_session
    async def delete(self, session: AsyncSession = None) -> None:
        await session.delete(self)
        await session.commit()

    def dict(self) -> dict:
        data = self.__dict__
        data['id'] = data['pk']
        del data['pk']
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


class Category(Base):
    name = Column(VARCHAR(64), nullable=False, unique=True)


class Product(Base):
    name = Column(VARCHAR(128), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
    is_published = Column(BOOLEAN, default=False)

    @property
    def category(self) -> Category:
        with self.session() as session:
            return session.get(Category, self.category_id)

# latte = Product(name='Latte', price=5.5, category_id=1, is_published=True)
# latte.save()
# cat = Category.get(1)
# print(cat.dict())
# latte = Product.get(1)
# latte.delete()
# print(latte.category_id)
# print(latte.category.name)
# print(Category.select())
# engine = create_engine('postgresql://belbank:belbank@localhost:5432/bank')
# session = sessionmaker(bind=engine)

# with session() as s:
#     cat = Category(name='Coffee')
#     s.add(cat)
#     s.commit()
#     s.refresh(cat)
#     print(cat.pk, cat.name)

# with session() as s:
#     cat = s.get(Category, 1)
#     print(cat.__dict__)
    # cat.name = 'Tea'
    # s.add(cat)
    # s.commit()
    # print(cat.name, cat.pk)
    # objs = s.execute(
    #     select(Category)
    #     .order_by(Category.name.desc())
    #     .filter(
    #         or_(
    #             Category.name.like('%ff%'),
    #             Category.pk > 0
    #         )
    #     )
    # )
    # print(objs.all())
# FastApi
# Pydantic
# AioHTTP
# SQLAlchemy + alembic
# Celery(Kafka)
