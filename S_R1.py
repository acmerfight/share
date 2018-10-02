class Question(object):

    def __init__(self, question_id, data_formatting):
        self._question_id = question_id
        self._data_formatter = DataFormatter(data_formatting)

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


Question(question_id=1, data_formatting="PDF").get()
