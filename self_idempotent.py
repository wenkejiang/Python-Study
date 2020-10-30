# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/30 11:58 上午
@Auth ： 姜文科
@File ：self_idempotent.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

import os
import time
class SelfIdempotent(object):

    def make_self_num(self):
        for num in range(100, 1000):
            low = num % 10
            mid = num // 10 % 10
            high = num // 100
            if num == low ** 3 + mid ** 3 + high ** 3:
                print(num)

    def reversed_num(self):
        num = int(input('num = '))
        reversed_num = 0
        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10
        print(reversed_num)



    def main(self):
        content = '北京欢迎你为你开天辟地…………'
        while True:
            # 清理屏幕上的输出
            os.system('cls')  # os.system('clear')
            print(content)
            # 休眠200毫秒
            time.sleep(0.2)
            content = content[1:] + content[0]


if __name__ == "__main__":
    self = SelfIdempotent()
    # self.make_self_num()
    # self.reversed_num()
    self.main()

