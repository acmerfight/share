# coding=utf-8

from datetime import date


class Person(object):

    def __init__(self, birth_day, sex, children, lover):
        # self.__birth_day = birth_day
        # self.__sex = sex
        # self.__children = children
        self._birth_day = birth_day
        self._sex = sex
        self._children = children
        self.lover = lover

    @property
    def birth_day(self):
        return self._birth_day

    @property
    def age(self):
        today = date.today()
        if (today.month, today.day) > (self._birth_day.month, self._birth_day.day):
            return today.year - self._birth_day.year
        else:
            return today.year - self._birth_day.year - 1

    @property
    def sex(self):
        return self._sex

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = children

    # def add_child(self, child):
    #     self._children.append(child)



# birth_day = date(1990, 1, 1)
# sex = True
# children = []
# person = Person(birth_day, sex, children)
