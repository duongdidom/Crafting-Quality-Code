import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stocksummary_1(self):
        """
        Test stock_price_summary where list is empty
        """
        actual = a1.stock_price_summary([])
        expected = (0,0)
        self.assertEqual(expected, actual)

    def test_stocksummary_2(self):
        """
        Test stock_price_summary where list contains all zeros
        """
        actual = a1.stock_price_summary([0,0,0])
        expected = (0,0)
        self.assertEqual(expected, actual)

    def test_stocksummary_3(self):
        """
        Test stock_price_summary where list contains one zero
        """
        actual = a1.stock_price_summary([0])
        expected = (0,0)
        self.assertEqual(expected, actual)
        
    def test_stocksummary_4(self):
        """
        Test stock_price_summary where list contains one negative
        """
        actual = a1.stock_price_summary([-1])
        expected = (0,-1.0)
        self.assertEqual(expected, actual)
        
    def test_stocksummary_5(self):
        """
        Test stock_price_summary where list contains one positive
        """
        actual = a1.stock_price_summary([0.10])
        expected = (0.1,0)
        self.assertEqual(expected, actual)
        
    def test_stocksummary_6(self):
        """
        Test stock_price_summary where list contains all negative numbers
        """
        actual = a1.stock_price_summary([-0.01, -0.11, -0.2, -0.03])
        expected = (0,-0.35)
        self.assertEqual(expected, actual)

    def test_stocksummary_7(self):
        """
        Test stock_price_summary where list contains all positive numbers
        """
        actual = a1.stock_price_summary([0.01, 0.11, 0.2, 0.03])
        expected = (0.35, 0)
        self.assertEqual(expected, actual)

    def test_stocksummary_8(self):
        """
        Test stock_price_summary where list contains positive, negative and zero
        """
        actual = a1.stock_price_summary([0.03, 0, 0.02, -0.03])
        expected = (0.05, -0.03)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
