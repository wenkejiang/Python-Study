# -*- coding: utf-8 -*-
"""
@Time ： 2020/10/30 3:00 下午
@Auth ： 姜文科
@File ：person.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()

    person.name="百元房"
    person.age = 22
    person.play()

    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()