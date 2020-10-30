# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/30 11:05 上午
@Auth ： 姜文科
@File ：game.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import random


class NumGame(object):

    def doGame(self):
        number = random.randint(1, 100)
        count = 0
        while True:
            count += 1
            answer = int(input("请输入。。。。"))
            if number > answer:
                print("输入的数字小了")
            elif number < answer:
                print("输入的数字大了")
            else:
                print("恭喜你，答对了")
                break
        print("您答了%d" % count + "次")
        if count > 5:
            print("你的智商很捉急")


if __name__ == "__main__":
    num = NumGame()
    num.doGame()
