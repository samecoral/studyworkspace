# 学习自定义函数
def sum_two_num(num1, num2):
    "对两个数相加"
    return num1 + num2


# 调用函数
print(sum_two_num(1, 90))


def sum_two_num(num1, num2):
    if (not isinstance(num1, (int, float)) or not isinstance(num2, (int, float))):
        raise TypeError('类型错误')
    return num1 + num2


# print(sum_two_num('a', 'b'))


# 返回两个值
def divide_two_num(num1, num2):
    return (num1 / num2), (num1 % num2)


print(divide_two_num(3, 2))
tuple1 = divide_two_num(3, 2)

print(1.1 + 4.399)
print(4.1 + 5.329)

from decimal import Decimal

a = Decimal('1.1')
b = Decimal('4.399')
print(a + b)
from decimal import getcontext
getcontext().prec = 3

print(10/3)


def change_num( b):
    b = 1000


a = 100
change_num(a)
print(a)


def change_list(list1):
    print('传入的初始list {}'.format(list1))
    list1.append(1000)
    print('改变之后的list{}'.format(list1))



lista = [1,10,98,75,33]
change_list(lista)
print(lista)