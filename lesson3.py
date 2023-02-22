# # n = 3
# #
# # users = {i: {'name': input(f'name {i}: '), 'email': input(f'email {i}: ')} for i in range(n)}
# # print(users)
#
#
# # from itertools import zip_longest
# #
# # numbers = iter([*range(2, int(input()) + 1, 2)])
# # numbers = list(zip_longest(numbers, numbers, numbers, numbers, numbers))
# # print(numbers)
#
# # def multiply(a, c=4, b=None):
# #     res = a * c
# #     return res
#
#
# # a = multiply(4, b=8)
# # b = multiply(3, 7)
# # print(a)
#
# # def foo(a, b=None):
# #     if b is None:
# #         b = []
# #     b.append(a)
# #     return b
# #
# #
# # print(foo(4))
# # print(foo(4))
#
#
# # def bar(*args):
# #     print(args)
#
#
# # bar(3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3)
#
#
# # def baz(**kwargs):
# #     print(kwargs)
# #
# #
# # baz(a=5, b=4, c=3)
#
# # def main(a, b=4, *args, c=None, **kwargs):
# #     print(a)
# #     print(b)
# #     print(c)
# #     print(args)
# #     print(kwargs)
# #
# #
# # main(1, 2, 3, 4, 5, 6, 7, 8, c=9, d=0)
#
#
# # def main():
# #     return 4, 5
# #
# # print(main())
#
# # def baz():
# #     print('baz')
# #
# #
# # def foo():
# #     baz()
# #     def bar():
# #         print('bar')
# #     bar()
# #
# # a = 5
# #
# #
# # def foo():
# #     a = 4
# #     def baz():
# #         nonlocal a
# #         print(a)
#
# # a = 4
# # b = 6
# #
# #
# # def multiply(a, b):
# #     c = None
# #     print(locals())
# #     return a * b
# #
# #
# # name = 'multiply'
# # print(globals()[name](5, 8))
#
# #
# # def foo(a):
# #     def bar(b):
# #         return a * b
# #     return bar
# #
# #
# # res = foo(8)
# # print(res(6))
#
# # def foo():
# #     print('foo')
# #
# #
# # def bar(func):
# #     func()
# #
# #
# # bar(foo)
#
#
# # multiply = lambda a, b: a * b
# #
# # print(multiply(5, 8))
#
#
# # words = ['age', 'Bread', 'Python', 'pycharm']
# # # ['age', 'bread', 'python', 'pycharm']
# # words.sort(key=lambda x: x.lower())
# # print(words)
#
#
# # numbers = [1, 6, 3, '9', '5', '3']
# # numbers.sort(key=lambda x: str(x))
# # print(numbers)
#
#
# # numbers = ['3', '1', '8', '4', '-3', '-2']
# # result = [*map(lambda x: abs(int(x)), numbers)]
# # print(result)
# # result = []
# # for number in numbers:
# #     number = abs(int(number))
# #     result.append(number)
# # print(result)
#
# # objs = [6, 2, 4, 2, 8, 4, 3, 5, 34, 98, 12, 34, 56, 23, 45]
# # result = [*filter(lambda x: x % 2 == 0, objs)]
# # print(result)
#
# # text = 'Hello'
# # numbers = [1, 2, 3, 4]
# # objs = (True, False, None)
# # result = [*zip(text, numbers, objs)]
# # print(result)
# # from functools import reduce
# #
# #
# # numbers = ['2', '3', '4', '5', '6', '7']
# # res = reduce(lambda x, y: int(x) * int(y), numbers)
# # print(res)
#
# # from itertools import *
# #
# # numbers = [1, 2, 3, 4, 5, 6]
# # print(*dropwhile(lambda x: x < 3, numbers))
# # print(*takewhile(lambda x: x < 3, numbers))
#
# # numbers = [1, 2, 3, 4, 5, 6, 7]
# # a = iter(numbers)
# # for i in a:
# #     if i == 4:
# #         break
# #     print(f'first {i=}')
# #
# # for i in a:
# #     print(f'second {i=}')
#
#
# # db = ['1', '2', '3', '4', '5', '6', '7']
# #
# #
# # def get_obj_from_db():
# #     for obj in db:
# #         yield obj
# #
# #
# # res = get_obj_from_db()
# # for i in res:
# #     print(i)
#
# # def my_range(start, stop, step):
# #     while True:
# #         start += step
# #         if start < stop:
# #             yield start
# #         else:
# #             break
# #
# #
# # for i in my_range(0, 10, 1):
# #     print(i)
#
# # from sys import getrecursionlimit, setrecursionlimit
#
#
# # numbers = [1, 2, 3, 4, [5, 6, 7, 3, 4, [6, 3, 4, 32, 4, 23, [5, 3, 4, 2, 3, ], [6, 4, 5, 2, 4, ], 6, 34, 6, 34, 6, [5, 2, 4, 32, 4, 3, [7, 4, 6, 4, 5]]]]]
# #
# #
# # def recursive_multiply(numbers):
# #     res = 1
# #     for number in numbers:
# #         if isinstance(number, list):
# #             res *= recursive_multiply(number)
# #         else:
# #             res *= number
# #     return res
# #
# #
# # print(recursive_multiply(numbers))
#
# def decorator(func):
#     def wrapper(a, b):
#         if not isinstance(a, int | float):
#             raise TypeError
#         if not isinstance(b, int | float):
#             raise TypeError
#         a += 1
#         b += 1
#         res = func(a, b)
#         return f'{res=}'
#     return wrapper
#
#
# # @decorator
# # def multiply(a, b):
# #     return a * b
# #
# #
# # decorated_multiply = decorator(multiply)
# #
# #
# # print(multiply(4, 5))
# # print(decorated_multiply(4, 5))
#
#
# def dispatcher(c, d):
#     def decorator(func):
#         def wrapper(a, b):
#             a += c
#             b += d
#             res = func(a, b)
#             return f'{res=}'
#         return wrapper
#     return decorator
#
#
# @dispatcher(2, 3)
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(3, 4))

from string import printable


# TODO протокол SMS способен передавать 140 байт информации
#  символы входящие в ASCII занивают по 1 байту, русские буквы по 2 байта
#  на вход функции, поступает текст, необходимо сказать на сколько сообщение необходимо разбить
#  текст чтобы его отправить по протоколу SMS


def split_sms(text):
    text = text.encode()
    bytes_count = len(text)
    # bytes_count = 0
    # for el in text:
    #     if el in printable:
    #         bytes_count += 1
    #     else:
    #         bytes_count += 2
    sms_count = bytes_count / 140
    if sms_count.is_integer():
        return int(sms_count)
    else:
        return int(sms_count) + 1


# TODO bin(ord('A')) - позволяет получить двоичное представление строкового символа
#  необходимо реализовать кодирование информации с помощью шифра Вернама
#  На вход функции поступает 2 строки - сообщение и ключ
#  Ключ и сообщение обязаны быть одинаковой длины
#  Кодирование с помощью шифра вернама происходит путем сравнивания бит информации
#  Если бит есть в одном, но нет в другом,  то бит копируется
#  ПРИМЕР: сообщение: LONDON ключ: SYSTEM
#  LONDON: 01001100 01001111 01001110 01000100 01001111 01001110
#  SYSTEM: 01010011 01011001 01010011 01010100 01000101 01001101
#  RESULT: 00011111 00010110 00011101 00010000 00001010 00000011


# def encode_vernama(message: str, key: str) -> str:
    # bin_message = ''
    # for i in message:
    #     i = bin(ord(i))[2:].zfill(8)
    #     bin_message += i
    # bin_key = ''
    # for i in key:
    #     i = bin(ord(i))[2:].zfill(8)
    #     bin_key += i
    # result = ''
    # for i in range(len(bin_message)):
    #     if bin_message[i] == bin_key[i]:
    #         result += '0'
    #     else:
    #         result += '1'
    # return result


def encode_vernama(message: str, key: str) -> str:
    message = map(lambda x: ord(x), message)
    key = map(lambda x: ord(x), key)
    z = zip(message, key)
    result = map(lambda x: x[0] ^ x[1], z)
    return ' '.join(map(lambda x: bin(x)[2:].zfill(8), result))


# print(encode_vernama('LONDON', 'SYSTEM'))

# TODO На вход функции поступает список чисел
#  Реализовать пузырьковый метод сортировки

def bubble_sort(numbers: list[int]) -> list[int]:
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# TODO На вход функции поступает отсортированный список чисел и искомое число
#  вернуть индекс вхождения искомого числа, полученного путем бинарного поиска


def binary_find(numbers: list[int], number: int) -> int:
    start = 0
    stop = len(numbers)
    while numbers[(start + stop) // 2] != number:
        if number > numbers[(start + stop) // 2]:
            start = (start + stop) // 2
        else:
            stop = (start + stop) // 2
    return (start + stop) // 2


# print(binary_find([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
