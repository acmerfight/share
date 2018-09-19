# coding=utf-8

from datetime import date


class Person(object):

    def __init__(self, birth_day, sex, children):
        self.birth_day = birth_day
        self.sex = sex
        self.children = children

    def compute_age(self):
        today = date.today()
        if (today.month, today.day) > (self.birth_day.month, self.birth_day.day):
            return today.year - self.birth_day.year
        else:
            return today.year - self.birth_day.year - 1


birth_day = date(1989, 1, 1)
sex = True
children = []
person = Person(birth_day, sex, children)

# case one
person.compute_age = 18
person.children = [1]
person.sex = False


# case two
birth_day = person.birth_day
birth_day.replace(year=2000)
print(birth_day)
