class Question(object):

    def __init__(self, question_id, data_formatter):
        self._question_id = question_id
        self._data_formatter = data_formatter

    def get(self):
        self._get_data()
        return self._data_formatter.format()

    def _get_data(self):
        # connect_MySQL
        # get_data_from_MySQL
        # connect_Redis
        # get_data_from_Redis
        pass


class DataFormatter(object):

    def __init__(self, data_formatting):
        self._data_formatting = data_formatting

    def format(self):
        pass

data_formatter = DataFormatter(data_formatting="PDF")
Question(question_id=1, data_formatter=data_formatter).get()

