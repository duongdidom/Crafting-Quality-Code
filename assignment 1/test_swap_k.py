import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swapK_1(self):
        """
        Test swap_k with k = 0
        """
        L_test = [1, 2, 3, 4, 5, 6]
        L_expected = [1, 2, 3, 4, 5, 6]
        
        self.assertEqual(L_expected, a1.swap_k(L_test, 0))

    def test_swapK_2(self):
        """
        Test swap_k with length of list is odd 
        """
        L_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        L_expected = [6, 7, 8, 9, 5, 1, 2, 3, 4]
        
        self.assertEqual(L_expected, a1.swap_k(L_test, 4))

    def test_swapK_3(self):
        """
        Test swap_k with length of list is even 
        """
        L_test = [1, 2, 3, 4, 5, 6]
        L_expected = [5, 6, 3, 4, 1, 2]
        
        self.assertEqual(L_expected, a1.swap_k(L_test, 2))

    def test_swapK_4(self):
        """
        Test swap_k with k = 1
        """
        L_test = [1, 2, 3, 4, 5, 6]
        L_expected = [6, 2, 3, 4, 5, 1]
        
        self.assertEqual(L_expected, a1.swap_k(L_test, 1))


if __name__ == '__main__':
    unittest.main(exit=False)
