# # # # # # # # # # # # # # # # # # # # # # # numbers = [2, 4, 2, 3, 'hello', True]
# # # # # # # # # # # # # # # # # # # # # # # print(len(numbers))
# # # # # # # # # # # # # # # # # # # # # # # text = 'hello'
# # # # # # # # # # # # # # # # # # # # # # # letters = list(text)
# # # # # # # # # # # # # # # # # # # # # # # print(letters)
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # numbers = [2 for i in range(10)]
# # # # # # # # # # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # numbers = [12, 12, 12]
# # # # # # # # # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # # # # # # # # # del numbers[1]
# # # # # # # # # # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # # # # # # # # # number = numbers.pop(1)
# # # # # # # # # # # # # # # # # # # # # # # print(number)
# # # # # # # # # # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # # # # # # # # numbers.remove(12)
# # # # # # # # # # # # # # # # # # # # # # # numbers.remove(12)
# # # # # # # # # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # numbers = [1, 2, 3, 4, 5, 6]
# # # # # # # # # # # # # # # # # # # # # del numbers[1:4]
# # # # # # # # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # lst2 = ['Python', 'Pycharm']
# # # # # # # # # # # # # # # # # # # # lst = ['Hello', 'World']
# # # # # # # # # # # # # # # # # # # # lst += lst2
# # # # # # # # # # # # # # # # # # # # print(lst * 2)
# # # # # # # # # # # # # # # # # # # # # lst3 = lst + lst2
# # # # # # # # # # # # # # # # # # # # # print(lst)
# # # # # # # # # # # # # # # # # # # # # print(lst2)
# # # # # # # # # # # # # # # # # # # # # print(lst3)
# # # # # # # # # # # # # # # # # # # # # lst.extend(lst2)
# # # # # # # # # # # # # # # # # # # # # print(lst)
# # # # # # # # # # # # # # # # # # # # # lst.insert(1, 'New')
# # # # # # # # # # # # # # # # # # # # # print(lst)
# # # # # # # # # # # # # # # # # # # # # lst.append([1, 2, 3])
# # # # # # # # # # # # # # # # # # # # # print(lst[2][1])
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # numbers = ['Hello', 'World']
# # # # # # # # # # # # # # # # # # # print(numbers[1])
# # # # # # # # # # # # # # # # # # # numbers[1] = None
# # # # # # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # numbers = [3, 5, 2, 4, 3, 8, 5, 7, -45]
# # # # # # # # # # # # # # # # # # numbers.sort()
# # # # # # # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # # # # # # result = [*sorted(numbers)]
# # # # # # # # # # # # # # # # # # # print(result)
# # # # # # # # # # # # # # # # # # words = ['Hello', 'hey', 'python', 'Pycharm', 'age']
# # # # # # # # # # # # # # # # # # words.sort(key=len)
# # # # # # # # # # # # # # # # # # print(words)
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # lst = [1, 2, 3, 4]
# # # # # # # # # # # # # # # # # lst2 = list(lst)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # from copy import deepcopy
# # # # # # # # # # # # # # # # lst = [1, 2, 3, 4, [5, 6, 7, 8]]
# # # # # # # # # # # # # # # # lst2 = deepcopy(lst)
# # # # # # # # # # # # # # # # lst2[4].append(9)
# # # # # # # # # # # # # # # # print(lst)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # words = ('hello')
# # # # # # # # # # # # # # # # print(words)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # tup = (1, 2, 3, 4, [5, 6, 7, 8])
# # # # # # # # # # # # # # # del tup[4][1]
# # # # # # # # # # # # # # # # tup[4].append(9)
# # # # # # # # # # # # # # # # print(tup)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # a = [1, 2, 3, 4]
# # # # # # # # # # # # # # b = [5, 6, 7, a]
# # # # # # # # # # # # # # del b[3]
# # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # #
# # # # # # # # # # # # # data = {
# # # # # # # # # # # # #     'name': 'Alex',
# # # # # # # # # # # # #     'age': 34,
# # # # # # # # # # # # #     'city': 'Minsk',
# # # # # # # # # # # # # }
# # # # # # # # # # # # # # data['name'] = 'Pavel'
# # # # # # # # # # # # # # print(data)
# # # # # # # # # # # # # data['lang'] = 'ru'
# # # # # # # # # # # # # print(data)
# # # # # # # # # # # #
# # # # # # # # # # # # # data = dict([('name', 'Alex'), ('age', 34), ('city', 'Minsk')])
# # # # # # # # # # # # # print(data)
# # # # # # # # # # # #
# # # # # # # # # # # # keys = ('name', 'age', 'city')
# # # # # # # # # # # # values = ('alex', 34, 'Minsk')
# # # # # # # # # # # # data = {keys[i]: values[i] for i in range(len(keys))}
# # # # # # # # # # # # print(data)
# # # # # # # # # # #
# # # # # # # # # # # data = dict.fromkeys(('name', 'age', 'city'))
# # # # # # # # # # # print(data)
# # # # # # # # # #
# # # # # # # # # data = {
# # # # # # # # #     'name': 'Alex',
# # # # # # # # #     'age': 34,
# # # # # # # # #     'city': 'Minsk',
# # # # # # # # # }
# # # # # # # # # # print(data.keys())
# # # # # # # # # # print(data.values())
# # # # # # # # # # print(data.items())
# # # # # # # # # # # print(data['lang'])
# # # # # # # # # # # print(data.get('city', 'Не указано!'))
# # # # # # # # # # print(data.setdefault('lang', 'Не указано!'))
# # # # # # # # # # print(data)
# # # # # # # # # #
# # # # # # # # # # value = data.pop('city', None)
# # # # # # # # # # print(value)
# # # # # # # # #
# # # # # # # # data = {
# # # # # # # #     'name': 'Alex',
# # # # # # # #     'age': 34,
# # # # # # # #     'city': 'Minsk',
# # # # # # # # }
# # # # # # # # new_data = {
# # # # # # # #     'city': 'Mogilev',
# # # # # # # #     'lang': 'ru'
# # # # # # # # }
# # # # # # # # # data.update(new_data)
# # # # # # # # # print(data)
# # # # # # # # # result = data | new_data
# # # # # # # # # print(data)
# # # # # # # # # print(new_data)
# # # # # # # # # print(result)
# # # # # # # # data |= new_data
# # # # # # #
# # # # # # # # data = {1, 2, 3, 4}
# # # # # # # # data = set('hello')
# # # # # # # # print(type(data))
# # # # # # # # print(data)
# # # # # # #
# # # # # # # s1 = {5, 7, 6}
# # # # # # # s2 = {5, 6, 7, 8, 4}
# # # # # # # # print(s1.isdisjoint(s2))
# # # # # # # # print(s1.issubset(s2))
# # # # # # # # print(s1 <= s2)
# # # # # # # print(s1.union(s2))
# # # # # # # print(s2.union(s1))
# # # # # # # print(s2 | s1)
# # # # # #
# # # # # # from collections import *
# # # # # #
# # # # # #
# # # # # # # text = 'hello world'
# # # # # # # text2 = 'hello python'
# # # # # # # text_counter = Counter(text)
# # # # # # # text_counter2 = Counter(text2)
# # # # # # # print(text_counter)
# # # # # # # print(text_counter2)
# # # # # # # print(text_counter - text_counter2)
# # # # # # # text_counter.subtract(text_counter2)
# # # # # # # print(text_counter)
# # # # # # # print([*text_counter.elements()])
# # # # # #
# # # # # # # q = deque([1, 2, 3, 4, 5, 6, 7])
# # # # # # # q.rotate(-2)
# # # # # # # print(q)
# # # # # #
# # # # # # # data = defaultdict(list)
# # # # # # # data['key'].append(1)
# # # # # # # print(data['key2'])
# # # # # # # print(data)
# # # # # #
# # # # # #
# # # # # # # keys = ('name', 'age', 'city')
# # # # # # #
# # # # # # # User = namedtuple('User', keys)
# # # # # # # vasya = User('vasya', 34, 'minsk')
# # # # # # # print(vasya.name)
# # # # # # # print(vasya._asdict())
# # # # # #
# # # # # # data1 = {
# # # # # #     'a': 1,
# # # # # #     'b': 2
# # # # # # }
# # # # # # data2 = {
# # # # # #     'b': 5,
# # # # # #     'c': 3,
# # # # # #     'd': 4
# # # # # # }
# # # # # # chain = ChainMap(data1, data2)
# # # # # # chain.parents['b'] = 8
# # # # # # print(data2)
# # # # # # print(chain.parents['b'])
# # # # #
# # # # # text = 'hello'
# # # # # data = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# # # #
# # # # a = int(input())
# # # # if a % 2:
# # # #     print('odd')
# # # # elif a == 0:
# # # #     print('Zero')
# # # # else:
# # # #     print('even')
# # # #
# # # # users = []
# # # # if users:
# # # #     pass
# # #
# # # # a = 4
# # # # if isinstance(a, int | float):
# # # #     pass
# # #
# # # # a = int(input())
# # # # a = 'No' if a % 2 else 'Yes' if a != 0 else 'Zero'
# # # # if a % 2:
# # # #     is_even = 'No'
# # # # elif a == 0:
# # # #     is_even = 'Zero'
# # # # else:
# # # #     is_even = 'Yes'
# # #
# # # x = True
# # # y = False
# # # z = False
# # # if not x or y:  # 0 + 0 = 0
# # #     print(1)
# # # elif not x or not y and z:  # 0 + 1 * 0 = 0 + 0 = 0
# # #     print(2)
# # # elif not x or y or not y and x:  # 0 + 0 + 1 * 1 = 0 + 0 + 1 = 1
# # #     print(3)
# # # else:
# # #     print(4)
# #
# # # str list tuple set frozenset dict
# # # text = 'hello world'
# # # for i in text:
# # #     print(i)
# #
# # # for i, j in enumerate(text):
# # #     print(i, j)
# #
# # # for i in range(len(text)):
# # #     print(text[i])
# #
# # # data = {
# # #     'key1': 'val1',
# # #     'key2': 'val2',
# # #     'key3': 'val3',
# # # }
# # # for key, val in data.items():
# # #     print(key, val)
# #
# # # for i in range(10):
# # #     if i == 10:
# # #         break
# # #     print(i)
# # # else:
# # #     print('finish')
# #
# # # objs = [2, 3, 4, 'hello', 'python', 5, 6]
# # # for obj in objs[::-1]:
# # #     if not isinstance(obj, str):
# # #         objs.remove(obj)
# # # print(objs)
# # # for obj in objs.copy():
# # #     objs.append(obj)
# # # print(objs)
# # from itertools import *
# #
# # # for i in count(0, 2):
# # #     print(i)
# #
# # # text = 'hello'
# # # for i in cycle(text):
# # #     print(i)
# #
# # # for i in repeat(text, 3):  # ['hello', 'hello', 'hello']
# # #     print(i)
# #
# # # print([*accumulate([1, 2, 3, 4, 5, 6])])
# # # print([*chain([1, 2, 3], [4, 5, 6])])
# # # print([*chain.from_iterable([[1, 2, 3], [5, 6, 7]])])
# # # numbers = [*range(100)]
# # # for i in islice(reversed(numbers), 2, 20, 2):
# # #     print(i)
# # # for i in numbers[2:20:2]:
# # #     print(i)
# #
# # # print(*combinations('abcd', 2))
# # # print(*combinations_with_replacement('abcd', 2))
# # # print(*product('abcd', repeat=2))
# #
# # # numbers = [i**2 for i in range(10) if i % 2]
# # # for i in range(10):
# # #     if i % 2:
# # #         numbers.append(i**2)
# #
# # # numbers = [2 for _ in range(100)]
# # # for i in range(100):
# # #     numbers.append(2)
# #
# # # print(*range(10))
# #
# # for i in range(10):
# #     pass
# #
# # for i in range(20):
# #     print(i)
#
# # print(all([1, 2, 3, 4, 9]))
# # print(any([0, 0, 0]))
#
# # print(a := input())
# # print(a)
#
# # a = int(input())
# # if (a := int(input())) % 2:
# #     print('odd')
# # else:
# #     print('even')
#
# # TODO Переспрашивать у пользователя данные с клавиатуры пока он не введет число
# # number = input('enter number: ')
# # while not number.isdigit():
# #     number = input('try again: ')
#
# # while not (number := input('enter number: ')).isdigit(): ...
#
# # print(bool(...))
#
# # number = [1, 2, 3]
# # a, b, c = number
# # while ...:
# #     print('вечный цикл')
#
# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# # except ValueError:
# #     print('не число')
# # except ZeroDivisionError:
# #     print('на 0 делить нельзя')
# except Exception as e:
#     print(e)
#
# else:
#     print('ошибок не  было')
# finally:
#     print('в любом случае')


# raise ValueError('ошибка')


# try:
#     exit()
# except SystemExit:
#     print('exit')

# numbers = [1, 2, 3, 4]
# reversed_numbers = reversed(numbers)
# print(list(reversed_numbers))
# print(list(reversed_numbers))

# N = 44
# 2 4 6 8 10
# 12 14 16 18 20
# 22 24 26 28 30
# 32 34 36 38 40
# 42 44


# TODO Вводится число найти его максимальную цифру: 583 -> 8
# number = input()
# max_num = max(number)
# print(max_num)

# TODO Есть монеты наминалом 25 10 5 1
#  Вводится сумма, сколько минимальное количество монет необходимо чтобы представить сумму
#  63 -> 25 + 25 + 10 + 1 + 1 + 1 = 6
# coins = (25, 10, 5, 2, 1)
# money = int(input())
# coins_total = 0
# for coin in coins:
#     coins_total += money // coin
#     money -= (money // coin) * coin
# print(coins_total)

# TODO Вводится сумма и процент по вкладу (вклад капитализации)
#  Через сколько лет сумма вклада удвоится
#  100 под 10% -> 8 лет
deposit = 100
percent = 0.1
target = deposit * 2
year = 0
while deposit < target:
    year += 1
    deposit *= 1 + percent
print(year)
