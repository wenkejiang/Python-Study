# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/30 11:41 上午
@Auth ： 姜文科
@File ：multiplication_table.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""


class Multiplication(object):

    def makeTable(self):
        for i in range(1, 10):
            for j in range(1, i + 1):
                print('%d * %d = %d' % (i, j, i * j), end='\t')
            print(" ")


if __name__ == "__main__":
    mu = Multiplication()
    mu.makeTable()
