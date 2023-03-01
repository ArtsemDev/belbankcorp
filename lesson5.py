# # file = open('input.txt', 'r', encoding='utf-8')
# # #
# # # # print(file.read())
# # # # print(file.readline())
# # # # print(file.readline())
# # # # print(file.readline())
# # # # print(file.readline())
# # # # print(file.readlines())
# # lines = [line.strip() for line in file if line.strip()]
# # print(file.read())
# # print(file.tell())
# # file.seek(0)
# # print(file.read())
# # # print(lines)
# # file.close()
# #
# # # text = ['Scutums mori!\n', 'Spatii de altus cobaltum, dignus rumor!']
# # #
# # #
# # # file = open('output.txt', 'w', encoding='utf-8')
# # # # file.write(text)
# # # file.writelines(text)
# # # file.close()
#
# #
# # with (
# #     open('input.txt', 'r', encoding='utf-8') as file,
# #     open('output.txt', 'w', encoding='utf-8') as out_file
# # ):
# #     print(file.readline())
# #     print(file.closed)
# # print(file.closed)
#
#
# #
# # from time import sleep
# # while True:
# #     with open('output.txt', 'a', encoding='utf-8') as file:
# #         file.write('1\n')
# #     sleep(1)
#
# # from json import dump, dumps, loads, load
# #
# # text = '''
# # {
# #   "name": "Alex",
# #   "age": 35,
# #   "is_human": true,
# #   "city": null,
# #   "languages": [
# #     "ru",
# #     "en"
# #   ]
# # }
# # '''
#
# # data = loads(text)
# # print(data)
# # with open('input.json', 'r', encoding='utf-8') as file:
# #     data = load(file)
# # print(data)
#
# # data = {
# #   "name": "Русские буквы",
# #   "age": 35,
# #   "is_human": True,
# #   "city": None,
# #   "languages": [
# #     "ru",
# #     "en"
# #   ]
# # }
# #
# # with open('output.json', 'w', encoding='utf-8') as file:
# #     dump(data, file, indent=2, ensure_ascii=False)
#
# from datetime import datetime
# from pprint import pprint
#
# from numpy import nan
# from pydantic import BaseModel, Field, validator, root_validator, EmailStr
# from pydantic.types import Decimal
#
#
# class TestModel(BaseModel):
#     id: int = Field(ge=1)
#
#
# class TransactionModel(BaseModel):
#     id: int = Field(gt=1)
#     transaction_time: datetime
#     description: str = Field(default=None)
#     amount: Decimal = Field(max_digits=8, decimal_places=2)
#     tests: list[TestModel]
#
#
# # data = {
# #     'id': -5,
# #     'transaction_time': 1677669874,
# #     'amount': 156.1212,
# #     'tests': [
# #         {
# #             'id': -4
# #         },
# #         {
# #             'id': 0
# #         }
# #     ]
# # }
# #
# # data = TransactionModel(**data)
# # print(data)
#
# db = ('vasya', 'petya')
#
#
# class RegisterFormModel(BaseModel):
#     username: str = Field(min_length=2)
#     password: str = Field(min_length=8)
#
#     @validator('username', pre=True)
#     def validate_username(cls, value):
#         if value in db:
#             raise ValueError('username is not unique')
#         return value
#
#     @root_validator
#     def validate(cls, values):
#         if values.get('username').lower() in values.get('password').lower():
#             raise ValueError('username in password')
#         return values
#
#
# # data = {
# #     'username': 'misha',
# #     'password': 'qwertymiccSHadfv'
# # }
# # RegisterFormModel(**data)
#
#
# class RecursiveModel(BaseModel):
#     name: str
#     descr: str
#     parent: "RecursiveModel" = Field(default=None)
#
#
# RecursiveModel.update_forward_refs()
#
# # data = {
# #     'name': 'name1',
# #     'descr': 'descr1',
# #     'parent': {
# #         'name': 'name2',
# #         'descr': 'descr2',
# #         'parent': {
# #             'name': 456
# #         }
# #     }
# # }
# # data = RecursiveModel(**data)
# # print(data)
#
# # import xml.etree.ElementTree as ET
# #
# #
# # parser = ET.parse('xmlingots.xml')
# # print(parser.getroot())
# # for tag in parser.getroot():
# #     print(tag.attrib)
# #     print(tag[0])
#
# # from xmltodict import parse
# #
# # with open('xmlingots.xml', 'r', encoding='utf-8') as file:
# #     data = parse(file.read())
# # pprint(data)
#
# from csv import reader, DictReader, writer, DictWriter
#
#
# # delimiter = ','
# #
# # with open('input.csv', 'r', encoding='utf-8') as file:
# #     keys = file.readline().strip().split(delimiter)
# #     data = []
# #     for line in file:
# #         data.append(dict(zip(keys, line.strip().split(delimiter))))
# # print(data)
#     # data = DictReader(file)
#     # for line in data:
#     #     print(line)
#
# # data = [
# #     {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'},
# #     {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'},
# #     {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'},
# # ]
# #
# # with open('output.csv', 'w', encoding='utf-8') as file:
# #     w = DictWriter(file, fieldnames=['key1', 'key2', 'key3'])
# #     w.writeheader()
# #     w.writerows(data)
# # from yaml import safe_dump, safe_load
# #
# #
# # with open('input.yaml', 'r', encoding='utf-8') as file:
# #     data = safe_load(file)
# # print(data)
#
# # from configparser import ConfigParser
# #
# # parser = ConfigParser()
# # parser.read('config.ini')
# # print(parser.options('SECOND'))
# # parser.set('SECOND', 'second_option1', 'new value')
# # with open('config.ini', 'w', encoding='utf-8') as file:
# #     parser.write(file, space_around_delimiters=False)
#
# # from openpyxl import load_workbook, Workbook
# #
# #
# # wb: Workbook = load_workbook('users.xlsx')
# # print(wb.sheetnames)
# # ws = wb.active
# # print(ws['A1'].value)
# # print(ws.cell(1, 1))
# # for line in ws:
# #     print(line)
#
#
# import pandas as pd
#
# # frame = pd.read_excel('users.xlsx')
# # frame.to_csv('users.csv', index=False)
#
# # frame = pd.DataFrame(
# #     {
# #         'name': ['petya', 'vasya', 'misha'],
# #         'age': [23, 54, 14],
# #         'city': ['minsk', 'brest', 'gomel']
# #     }
# # )
# # print(frame[frame['age'] > 20][frame['age'] < 55])
# # for user in frame.iloc:
# #     print(user['name'])
#
# from psycopg2 import connect
# from openpyxl import Workbook
# # # from psycopg2.extras import NamedTupleCursor
# #
# #
# conn = connect('postgresql://belbank:belbank@localhost:5432/bank')
# wb = Workbook()
# ws = wb.active
# with conn.cursor() as cur:
#     cur.execute('''SELECT * FROM users;''')
#     for obj in cur:
#         ws.append(obj)
#
# wb.save('db.xlsx')
# # with conn.cursor() as cur:
# #     cur.execute('''
# #         CREATE TABLE IF NOT EXISTS users(
# #             id BIGSERIAL PRIMARY KEY,
# #             name VARCHAR(64) NOT NULL,
# #             email VARCHAR(128) UNIQUE NOT NULL
# #         );
# #     ''')
# #     conn.commit()
#
# # with conn.cursor() as cur:
# #     cur.execute('''
# #         INSERT INTO users(name, email) VALUES(%s, %s);
# #     ''', ('vasya', 'vasya@email.com'))
# #     conn.commit()
# #
# # with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
# #     cur.execute('''
# #         SELECT * FROM users;
# #     ''')
# #     for i in cur:
# #         print(i)

# from pathlib import Path
#
# BASE_DIR = Path(__file__).resolve().parent

# from datetime import timedelta, datetime, date, time

#
# now = datetime.now().strftime('%A %d %m %Y %H:%M')
# print(now)

# text = 'Wednesday 01 03 2023 17:00'
# print(datetime.strptime(text, '%A %d %m %Y %H:%M'))

# d = datetime(year=2021, month=5, day=3)
# now = datetime.now()
# # print(now - d)
#
# delta = timedelta(days=365)
# print((now + delta) > now)
#
# from argparse import ArgumentParser
#
# parser = ArgumentParser()
# parser.add_argument('-p', '--port', default='8000', help='PORT')
# parser.add_argument('-d', '--debug', action='store_true', help='DEBUG MODE')
# args = parser.parse_args()
# print(args)
import logging
from datetime import datetime

logging.basicConfig(
    filename=f'{datetime.now().strftime("%d-%m-%Y")}.log',
    filemode='a',
    format='[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
    level=logging.INFO
)

logging.info('info message')
logging.warning('warning message')
logging.error('error message')
