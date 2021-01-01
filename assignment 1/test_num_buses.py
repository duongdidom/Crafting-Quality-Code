import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_numbuses_1(self):
        """ 
        Test num_buses with 0 people
        """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_numbuses_2(self):
        """ 
        Test num_buses with less than 50 people
        """
        actual = a1.num_buses(20)
        expected = 1
        self.assertEqual(expected, actual)

    def test_numbuses_3(self):
        """ 
        Test num_buses with 51 to 100 people
        """
        actual = a1.num_buses(63)
        expected = 2
        self.assertEqual(expected, actual)

    def test_numbuses_4(self):
        """ 
        Test num_buses with more than 100 people
        """
        actual = a1.num_buses(111)
        expected = 3
        self.assertEqual(expected, actual)

    def test_numbuses_5(self):
        """ 
        Test num_buses with more than 50 people and multiple of 50
        """
        actual = a1.num_buses(1000)
        expected = 20
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
