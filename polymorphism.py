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

    @abc.abstractmethod
    def qa_test(self):
        pass

    @abc.abstractmethod
    def release(self):
        pass


class LiveDevelopment(Development):

    def _step_1(self):
        print("step1")

    def _step_3(self):
        print("step3")


if __name__ == "__main__":
    ConcreteClass().run()