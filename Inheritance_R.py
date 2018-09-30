# coding=utf-8


class Stack(object):

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        self._items.pop()

