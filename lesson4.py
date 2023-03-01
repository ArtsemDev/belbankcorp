# # # """
# # #
# # # """
# # #
# # # # objs = [True, False, True, 1, 2, 3, 4, 'Hello', 'World', None]
# # # # objs = [*filter(lambda x: isinstance(x, str), objs)]
# # # # objs = [obj for obj in objs if isinstance(obj, str)]
# # # # print(objs)
# # # # for i in range(len(objs) - 1, -1, -1):
# # # #     if not isinstance(objs[i], str):
# # # #         del objs[i]
# # # # print(objs)
# # #
# # #
# # # class User:
# # #
# # #     a = 5
# # #
# # #     # Create New object
# # #     # def __new__(cls, *args, **kwargs):
# # #
# # #     # Принимает аргументы через скобки в момент объявления
# # #     # def __call__(self, *args, **kwargs):
# # #
# # #     def __init__(self, name, age, email):
# # #         self.first_name = name.title()
# # #         self.age = age
# # #         self.email = email.lower()
# # #
# # #     def dict(self):
# # #         return {
# # #             'name': self.first_name,
# # #             'age': self.age,
# # #             'email': self.email
# # #         }
# # #
# # #     @classmethod
# # #     def change_a(cls, value):
# # #         cls.a = value
# # #
# # #     @staticmethod
# # #     def bar():
# # #         print('bar')
# # #
# # #     def __str__(self):
# # #         return f'User: (name={self.first_name}, age={self.age}, email={self.email})'
# # #
# # #     def __eq__(self, other):
# # #         if isinstance(other, User):
# # #             return self.age == other.age
# # #         elif isinstance(other, (int, float)):
# # #             return self.age == other
# # #
# # #     def __add__(self, other):
# # #         if isinstance(other, User):
# # #             return self.age + other.age
# # #         elif isinstance(other, (int, float)):
# # #             return self.age + other
# # #
# # #     def __radd__(self, other):
# # #         return self.__add__(other)
# # #
# # #
# # # class Manager(User):
# # #
# # #     def dict(self):
# # #         data = super(Manager, self).dict()
# # #         data['salary'] = 1500
# # #         return data
# # #
# # # # vasya = User('vasya', 26, 'vasya@info.com')
# # # # petya = User('petya', 45, 'petya@info.com')
# # # # print(vasya + petya)
# # # # print(45 + vasya)
# # # # print(vasya == petya)
# # # # print(petya == 56)
# # # # print(vasya.dict())
# # # # vasya.a = 6
# # # # vasya.city = 'Minsk'
# # # # print(vasya.a)
# # # # User.a = 3
# # # # print(petya.a)
# # # # print(vasya.a)
# # # # print(User.a)
# # #
# # #
# # # # TODO Написать класс Rectangle
# # # #  Конструктор класса принимает координаты точек по диагонале (правая нижняя и левая верхняя
# # # #  или правая верхняя и левая нижняя)
# # # #  написать метод объекта preimeter возвращающий периметр получившегося прямоугольника
# # # #  написать метод объекта square возвращающий площать получившегося прямоугольника
# # #
# # #
# # # class Rectangle:
# # #
# # #     def __init__(self, x1, y1, x2, y2):
# # #         self.width = abs(x1 - x2)
# # #         self.height = abs(y1 - y2)
# # #
# # #     def perimeter(self):
# # #         return 2 * (self.width + self.height)
# # #
# # #     def area(self):
# # #         return self.width * self.height
# # #
# # #
# # # class Square(Rectangle):
# # #
# # #     def __init__(self, x1, y1, x2, y2, x3):
# # #         super().__init__(x1, y1, x2, y2)
# # #         self.x3 = x3
# # #
# # #
# # # # TODO Реализовать класс Category
# # # #  Создать атрибут класса categories (list)
# # # #  3.1 Написать метод класса add принимающий на вход название категории, если такой
# # # #  категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# # # #  индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# # # #  исключение ValueError
# # # #  3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# # # #  категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# # # #  IndexError
# # # #  3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# # # #  удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# # # #  индексе, ничего не делать, метод ничего возвращать не должен
# # # #  3.4 Написать метод класса update принимающий индекс категорий и новое название
# # # #  категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# # # #  учетом того, что имена категорий уникальны, если новое имя категории нарушает
# # # #  уникальность в списке категорий, вызвать исключение ValueError
# # #
# # #
# # # class Category:
# # #
# # #     categories = ['cat1', 'cat2', 'cat3']
# # #     i = -1
# # #
# # #     @classmethod
# # #     def add(cls, value: str) -> int:
# # #         """Добавление новой категории
# # #
# # #         :param value: название новой категории
# # #         :return: индекс новой категории
# # #         """
# # #         if value.title() not in cls.categories:
# # #             cls.categories.append(value.title())
# # #             return len(cls.categories) - 1
# # #         else:
# # #             raise ValueError('category is not unique')
# # #
# # #     @classmethod
# # #     def get(cls, i):
# # #         return cls.categories[i]
# # #
# # #     @classmethod
# # #     def delete(cls, i):
# # #         try:
# # #             del cls.categories[i]
# # #         except IndexError:
# # #             pass
# # #
# # #     @classmethod
# # #     def update(cls, i, value):
# # #         if i in range(len(cls.categories)):
# # #             if value.title() not in cls.categories:
# # #                 cls.categories[i] = value.title()
# # #             else:
# # #                 raise ValueError('category is not unique')
# # #         else:
# # #             return cls.add(value)
# # #
# # #     def __iter__(self):
# # #         return self
# # #
# # #     def __next__(self):
# # #         self.i += 1
# # #         if self.i in range(len(self.categories)):
# # #             return self.categories[self.i]
# # #         else:
# # #             self.i = -1
# # #             raise StopIteration
# # #
# # #
# # # # print(Category.add.__doc__)
# # # # categories = Category()
# # # # for category in categories:
# # # #     print(category)
# # #
# # #
# # # class A:
# # #     __name = 'A'
# # #
# # #
# # # class B:
# # #     __name = 'B'
# # #
# # #
# # # class C(A, B):
# # #     pass
# # #
# # #
# # # # print(C.mro())
# # #
# # #
# # # class Product:
# # #
# # #     @classmethod
# # #     def all(cls):
# # #         pass
# # #
# # #
# # # class User:
# # #
# # #     @classmethod
# # #     def all(cls):
# # #         pass
# # #
# # #
# # # def main(obj: Product | User):
# # #     if isinstance(obj, (Product, User)):
# # #         obj.all()
# # #     # if isinstance(obj, Product):
# # #     #     obj.get_products()
# # #     # elif isinstance(obj, User):
# # #     #     obj.get_users()
# # #
# # #
# # #
# #
# #
# # class DebitCard:
# #
# #     def __init__(self, card_number: str):
# #         self.__card_number = card_number
# #
# #     @property
# #     def card_number(self):
# #         return self.__card_number[:6] + '******' + self.__card_number[-4:]
# #
# #     @card_number.setter
# #     def card_number(self, value):
# #         if not isinstance(value, str):
# #             raise TypeError
# #         elif not value.isdigit():
# #             raise ValueError
# #         elif len(value) != 16:
# #             raise ValueError
# #         self.__card_number = value
# #
# #
# # # card = DebitCard(card_number='1234567891234567')
# # # print(card.card_number)
# # # card.card_number = '9876543215643215'
# #
# #
# # class Engine:
# #
# #     def __init__(self, volume):
# #         self.volume = volume
# #
# #
# # class Car:
# #
# #     def __init__(self, name, engine):
# #         self.name = name
# #         self.engine = engine
# #
# #
# # class Manufacture:
# #     cars = []
# #
# #     @classmethod
# #     def create_cars(cls, count):
# #         engines = [Engine(4.4) for _ in range(count)]
# #         cars = [Car('car', engine) for engine in engines]
# #         cls.cars.extend(cars)
# #         return cls.cars
# #
# # # engine = Engine(4.5)
# # # car = Car('BWM', engine)
# # # from dataclasses import dataclass
# # #
# # #
# # # @dataclass(frozen=True)
# # # class User:
# # #     name: str
# # #     age: int
# # #     email: str
# #
# #
# # # vasya = User('vasya', '34', 'vasya@info.com')
# # # vasya.name = 'Petya'
# # # print(vasya)
# #
# # #
# # # class User:
# # #
# # #     def __init__(self, name, age, email):
# # #         self.name = name
# # #         self.age = age
# # #         self.email = email
# # #
# # #     def __repr__(self):
# # #         return f'User: ({self.name=}, {self.age=}, {self.email=})'
# # #
# # #     def __setattr__(self, key, value):
# # #         raise AttributeError
# # #
# # #     def __delattr__(self, item):
# # #         raise AttributeError
# #
# #
# # from abc import ABC, abstractmethod
# #
# #
# # class Person(ABC):
# #
# #     def info(self):
# #         print('info')
# #
# #     @abstractmethod
# #     def dict(self, value):
# #         pass
# #
# #
# # class User(Person):
# #
# #     def dict(self, value):
# #         print({})
#
#
# from enum import Enum, IntEnum
#
#
# statuses = [('Approve', 1), ('Revoke', 2), ('Cancel', 3)]
#
# # OrderStatus = IntEnum('OrderStatus', statuses)
# #
# # # class OrderStatus(int, Enum):
# # #     Approve: int = 1
# # #     Revoke: int = 2
# # #     Cancel: int = 3
# #
# #
# # order_status = 2
# # # 1 - approve, 2 - revoke, 3 - cancel
# #
# # if order_status == OrderStatus.Approve:
# #     print('approve')
# # elif order_status == OrderStatus.Revoke:
# #     print('revoke')
# # from http import HTTPStatus
#
#
# name = 'Alex'
#
#
# def info(self):
#     return self.name
#
#
# Alex = type('Alex', (), {'name': name, 'info': info})
#
#
# a = Alex()
# # print(a.dir())
# # print(a.info())


# class MyMetaclass(type):
#     pass
#
#
# class MyClass(metaclass=MyMetaclass):
#     __metaclass__ = MyMetaclass


# TODO Написать класс RegisterForm
#  констурктор класса принимает аргументы username, password и объявляет атрибуты объекта
#  на их основе
#  написать метод объекта is_valid проверяющий атрибуты на критерии
#  1. username - строка, password - cтрока
#  2. длина username >= 2
#  3. длина password >= 8
#  4. password не должен содержать в себе username
#  5. password должен содержать хотя бы 1 большую букву и 1 цифру
#  Если 1 из пунктов нарешается, метод должен возвращать False, и True в противном случае


class RegisterForm:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid(self) -> bool:
        if not isinstance(self.username, str):
            return False
        elif len(self.username) < 2:
            return False
        if not isinstance(self.password, str):
            return False
        elif self.username.lower() in self.password.lower():
            return False
        elif len(self.password) < 8:
            return False
        is_digit = False
        is_upper_letter = False
        for el in self.password:
            if el.isdigit():
                is_digit = True
            elif el.isupper():
                is_upper_letter = True
        if is_digit and is_upper_letter:
            return True
        else:
            return False
# TODO Написать класс Numbers
#  Конструктор класса принимает список чисел numbers: list[int]
#  Написать метод average — возвращающий среднее арифметическое между всеми числами
#  Написать метод max_count — возвращающий число из списка, которое чаще встречается,
#  если таких чисел несколько, вывести среднее арифметическое среди таких чисел


class Numbers:

    def __init__(self, *args):
        self.numbers = args

    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def max_count(self):
        from collections import Counter
        counter = Counter(self.numbers)
        max_common = counter.most_common(1)[0][1]
        numbers = [*filter(lambda x: self.numbers.count(x) == max_common, self.numbers)]
        return sum(numbers) / len(numbers)


# n = Numbers(2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 2, 2, 3, 3)
# print(n.average())


from time import sleep
while True:
    with open('output.txt', 'r', encoding='utf-8') as file:
        print(file.read())
    sleep(2)
pi = 3.14159