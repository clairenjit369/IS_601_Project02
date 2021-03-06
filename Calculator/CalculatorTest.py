import unittest

from Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader('Tests\BasicFunctions\Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)
        test_data = CsvReader('Tests\BasicFunctions\Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader('Tests\BasicFunctions\Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)
        test_data = CsvReader('Tests\BasicFunctions\Division1.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)
        test_data = CsvReader('Tests\BasicFunctions\Square.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Results']) ** 2)
            self.assertEqual(self.calculator.result, int (row['Results']) ** 2)

    def test_square_root(self):
        self.assertEqual(self.calculator.squareRoot(4), 2)
        self.assertEqual(self.calculator.result, 2)
        test_data = CsvReader('Tests\BasicFunctions\Square Root.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squareRoot(row['Value 1']), float(row['Result']) ** 0.5)
            self.assertEqual(self.calculator.result, float (row['Result']) ** 0.5)


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)


if __name__ == '__main__':
    unittest.main()