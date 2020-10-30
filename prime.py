# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/30 11:51 上午
@Auth ： 姜文科
@File ：prime.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from math import sqrt


class Prime(object):

    def get_prime(self):
        num = int(input("请输入一个数字："))
        end = int(sqrt(num))
        is_prime = True
        for x in range(2, end + 1):
            if num % x == 0:
                is_prime = False
                break
        if is_prime and num != 1:
            print('%d是素数' % num)
        else:
            print('%d不是素数' % num)


if __name__ == "__main__":
    prime = Prime()
    prime.get_prime()
