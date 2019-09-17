import unittest
from unittest.mock import patch

from testing_python_lab2.services.convert_integer_context import ConvertIntegerContext
from testing_python_lab2.services.convert_integer_strategies import (
    ConvertToBinaryStrategy, ConvertToDecimalStrategy, ConvertToHexStrategy
)


class TestConvertInteger(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_convert_decimal_integer_to_binary(self):

        """
            Summary: Conversion of decimal integer to binary.
            Units under test: ConvertIntegerContext, ConvertToBinaryStrategy, ConvertIntegerStrategy
            Preconditions: None
            Parameters to test: correct operation of Strategy design pattern modules.
            Test scenario:
                Define concrete strategy;
                Define strategy context passing concrete strategy as argument;
                Call convert method of defined strategy;
                Compare output with a sample.
        """

        convert_to_binary_strategy = ConvertToBinaryStrategy()
        convert_integer_context = ConvertIntegerContext(convert_to_binary_strategy)
        binary_integer = convert_integer_context.execute_convert(69)
        self.assertEqual(binary_integer, '0b1000101')


    def test_convert_binary_integer_to_decimal(self):

        """
            Summary: Conversion of binary integer to decimal.
            Units under test: ConvertIntegerContext, ConvertToDecimalStrategy, ConvertIntegerStrategy
            Preconditions: None
            Parameters to test: correct operation of Strategy design pattern modules.
            Test scenario:
                Define concrete strategy;
                Define strategy context passing concrete strategy as argument;
                Call convert method of defined strategy;
                Compare output with a sample.
        """

        convert_to_decimal_strategy = ConvertToDecimalStrategy()
        convert_integer_context = ConvertIntegerContext(convert_to_decimal_strategy)
        decimal_integer = convert_integer_context.execute_convert('-0b11000010')
        self.assertEqual(decimal_integer, -194)


    def test_convert_binary_integer_to_hex(self):

        """
            Summary: Conversion of binary integer to hexadecimal.
            Units under test: ConvertIntegerContext, ConvertToHexStrategy, ConvertIntegerStrategy
            Preconditions: None
            Parameters to test: correct operation of Strategy design pattern modules.
            Test scenario:
                Define concrete strategy;
                Define strategy context passing concrete strategy as argument;
                Call convert method of defined strategy;
                Compare output with a sample.
        """

        convert_to_hex_strategy = ConvertToHexStrategy()
        convert_integer_context = ConvertIntegerContext(convert_to_hex_strategy)
        hexadecimal = convert_integer_context.execute_convert(2000)
        self.assertEqual(hexadecimal, '0x7d0')


    def test_convert_hex_to_decimal(self):

        """
            Summary: Conversion of hexadecimal to decimal.
            Units under test: ConvertIntegerContext, ConvertToDecimalStrategy, ConvertIntegerStrategy
            Preconditions: None
            Parameters to test: correct operation of Strategy design pattern modules.
            Test scenario:
                Define concrete strategy;
                Define strategy context passing concrete strategy as argument;
                Call convert method of defined strategy;
                Compare output with a sample.
        """

        convert_to_decimal_strategy = ConvertToDecimalStrategy()
        convert_integer_context = ConvertIntegerContext(convert_to_decimal_strategy)
        decimal_integer = convert_integer_context.execute_convert('0x7d0')
        self.assertEqual(decimal_integer, 2000)


    @patch("testing_python_lab2.services.convert_integer_strategies.ConvertToDecimalStrategy.convert")
    def test_convert_method_takes_correct_argument(self, mocked_conversion):

        """
            Summary: Conversion of binary integer to decimal.
            Units under test: ConvertIntegerContext, ConvertToDecimalStrategy, ConvertIntegerStrategy
            Preconditions: Mock covert() method of ConvertToDecimalStrategy class.
            Parameters to test: correct operation of Strategy design pattern modules.
            Test scenario:
                Define concrete strategy;
                Define strategy context passing concrete strategy as argument;
                Call convert method of defined strategy;
                Compare passed argument with a sample.
        """

        convert_to_decimal_strategy = ConvertToDecimalStrategy()
        convert_integer_context = ConvertIntegerContext(convert_to_decimal_strategy)
        convert_integer_context.execute_convert('-0b11000010')
        mocked_conversion.assert_called_with('-0b11000010')


    @patch("testing_python_lab2.services.convert_integer_strategies.ConvertToHexStrategy.convert")
    def test_convert_method_takes_wrong_argument(self, mocked_conversion):

        """
            Summary: Conversion of hexadecimal to decimal.
            Units under test: ConvertIntegerContext, ConvertToDecimalStrategy, ConvertIntegerStrategy
            Preconditions: Mock covert() method of ConvertToDecimalStrategy class.
            Parameters to test: correct operation of Strategy design pattern modules.
            Test scenario:
                Define concrete strategy;
                Define strategy context passing concrete strategy as argument;
                Call convert method of defined strategy;
                Compare passed argument with a sample.
        """
        mocked_conversion.return_value = '0x13'

        convert_to_hex_strategy = ConvertToHexStrategy()
        convert_integer_context = ConvertIntegerContext(convert_to_hex_strategy)

        value = convert_integer_context.execute_convert('wrong argument')
        result = ConvertToDecimalStrategy().convert(value)

        self.assertEqual(result, 19)