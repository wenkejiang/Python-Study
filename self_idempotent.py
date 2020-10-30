# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/30 11:58 上午
@Auth ： 姜文科
@File ：self_idempotent.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""


class SelfIdempotent(object):
    def make_self_num(self):
        for num in range(100, 1000):
            low = num % 10
            mid = num // 10 % 10
            high = num // 100
            if num == low ** 3 + mid ** 3 + high ** 3:
                print(num)


if __name__ == "__main__":
    self = SelfIdempotent()
    self.make_self_num()
