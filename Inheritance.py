# coding=utf-8


class Stack(list):

    def push(self, item):
        self.append(item)

    # 直接使用 list 的 pop 方法
    # def pop(self, index: int = ...):
    #     pass


class DictString(dict):

    def __setitem__(self, key, value):
        if (
            isinstance(key, str) and
            isinstance(value, str)
        ):
            super(DictString, self).__setitem__(key, value)
        else:

            raise TypeError("")


class Bird(object):

    name = "Bird"

    def fly(self):
        pass

    def run(self):
        print(self.name + " run")


class Ostrich(Bird):
    """
    can't fly
    """

    def laid_eggs(self):
        pass
