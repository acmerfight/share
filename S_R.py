# coding=utf-8


class Question(object):

    def __init__(self, question_id, data_formatting):
        self._question_id = question_id
        self._data_formatting = data_formatting

    def get(self):
        self._get_data()
        return self._format_data()

    def _get_data(self):
        # connect_MySQL
        # get_data_from_MySQL
        # connect_Redis
        # get_data_from_Redis
        pass

    def _format_data(self):
        # do something
        pass




