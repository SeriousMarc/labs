from abc import ABC, abstractmethod


class ConvertIntegerStrategy(ABC):
    @abstractmethod
    def convert(self, integer):
        pass


class ConvertToBinaryStrategy(ConvertIntegerStrategy):
    def convert(self, integer):
        """
            Method converts decimal integer to binary.
            :param integer: decimal integer to convert (int).
            :return: binary string (str).
        """

        return bin(int(integer))


class ConvertToHexStrategy(ConvertIntegerStrategy):
    def convert(self, integer):

        """
            Method converts decimal integer to hexadecimal.
            :param integer: decimal integer to convert (int).
            :return: hexadecimal string (str).
        """

        return hex(int(integer))


class ConvertToDecimalStrategy(ConvertIntegerStrategy):
    def convert(self, non_decimal_string):

        """
            Method converts non-decimal string to decimal.
            :param non_decimal_string: non-decimal integer to convert (str).
            :return: decimal integer (int).
        """

        return int(non_decimal_string, 0)
