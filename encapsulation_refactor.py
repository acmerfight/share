from datetime import date


class Person(object):

    def __init__(self, birth_day, sex, children):
        # self.__birth_day = birth_day
        # self.__sex = sex
        # self.__children = children
        self._birth_day = birth_day
        self._sex = sex
        self._children = children

    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, value):
        if value > date.today().day:
            raise ValueError("birth_day's value is invalid")
        self._birth_day = value

    @property
    def age(self):
        today = date.today()
        if (today.month, today.day) > (self._birth_day.month, self._birth_day.day):
            return today.year - self._birth_day.year
        else:
            return today.year - self._birth_day.year - 1

    # @property
    # def sex(self):
    #     return self._sex

    def is_male(self):
        return self._sex

    def is_female(self):
        return not self._sex


birth_day = date(1990, 1, 1)
sex = True
children = []
person = Person(birth_day, sex, children)
