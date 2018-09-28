# coding=utf-8

from datetime import date


class Person(object):

    def __init__(self, birth_day, sex, children, lover):
        self.birth_day = birth_day
        self.sex = sex
        self.children = children
        self.lover = lover
        self.age = self.compute_age()

    def compute_age(self):
        today = date.today()
        if (today.month, today.day) > (self.birth_day.month, self.birth_day.day):
            return today.year - self.birth_day.year
        else:
            return today.year - self.birth_day.year - 1


person = Person(date(1990, 1, 1), u"male", [], u"新垣结衣")

person.birth_day = date(1996, 1, 1)
person.children = [1]
person.sex = u"female"
person.lover = u"刘亦菲"
person.age = 18
