# coding=utf-8


class Stack(list):

    def push(self, item):
        self.append(item)

    # 直接使用 list 的 pop 方法
    # def pop(self, index: int = ...):
    #     pass


class Bird(object):

    name = "Bird"

    def fly(self):
        pass

    def run(self):
        print(self.name + " run")


class Ostrich(Bird):

    def laid_eggs(self):
        pass

