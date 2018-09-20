import abc


class Development(object):
    __metaclass__ = abc.ABCMeta

    def run(self):
        self.rfc_review()
        self.write_code()
        self.qa_test()
        self.release()

    @abc.abstractmethod
    def rfc_review(self):
        pass

    @abc.abstractmethod
    def write_code(self):
        pass

    @staticmethod
    def test():
        print("test")

    @abc.abstractmethod
    def release(self):
        pass


class LiveDevelopment(Development):

    def rfc_review(self):
        print("MySQL，HBase")

    def write_code(self):
        print("Java")

    def release(self):
        print("build APP, upload")


if __name__ == "__main__":
    LiveDevelopment().run()
