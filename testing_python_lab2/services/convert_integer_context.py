class ConvertIntegerContext(object):
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def execute_convert(self, integer):
        return self._strategy.convert(integer)
