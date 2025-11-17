# https://github.com/Alexander-Freedman/lab11-AF-WR
# Partner 1 Alexander Freedman
# Partner 2 William Ross



import unittest
import math
import calculator
class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(4, 9), 3)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.sub(10, 3), 7)
        self.assertEqual(calculator.add(4, 9), -5)
        self.assertEqual(calculator.add(0, 0), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.multiply(5, 3), 15)  # test pos
        self.assertEqual(calculator.multiply(-2, 10), -20)  # test neg
        self.assertEqual(calculator.multiply(7, 0), 0) # test 0

    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.multiply(10, 2), 5)  # test pos
        self.assertAlmostEqual(calculator.div(5, 2), 2.5) # test float
        with self.assertRaises(ZeroDivisionError): # test error catching
            calculator.div(10, 0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(calculator.log(2, 8), 3)
        self.assertTrue(math.isclose(calculator.log(10, 100), 2))
        self.assertTrue(math.isclose(calculator.log(3, 9), 2))


    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(-2, 8)
        with self.assertRaises(ValueError):
            calculator.log(2, -8)
        with self.assertRaises(ValueError):
            calculator.log(0, 5)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        # test common case
        self.assertEqual(calculator.hypotenuse(3, 4), 5)

        # test commonn case (5-12-13)
        self.assertEqual(calculator.hypotenuse(5, 12), 13)

        # test float
        self.assertAlmostEqual(calculator.hypotenuse(1, 1), 1.41421356)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        # test invalid case
        with self.assertRaises(ValueError):
            calculator.square_root(-9)
        # test perfect square
        self.assertEqual(calculator.square_root(16), 4)
        # Test non-perfect square
        self.assertAlmostEqual(calculator.square_root(2), 1.41421356)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()