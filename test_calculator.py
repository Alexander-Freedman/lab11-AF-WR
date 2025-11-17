import unittest
import pytest
import math
import calculator
class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        assert calculator.add(3, 4) == 7
        assert calculator.add(-2, 5) == 3

    def test_subtract(self): # 3 assertions
        assert calculator.sub(10, 3) == 7
        assert calculator.sub(4, 9) == -5
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with pytest.raises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self): # 3 assertions
        assert calculator.log(2, 8) == 3
        assert math.isclose(calculator.log(10, 100), 2)

    def test_log_invalid_base(self):
        with pytest.raises(ValueError):
            calculator.log(-2, 8)
        with pytest.raises(ValueError):
            calculator.log(2, -8)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()