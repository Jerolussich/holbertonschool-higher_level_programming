import unittest
max_integer = __import__('6-max_integer').max_integer


class tests(unittest.TestCase):

    def test_max_last_order(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_middle_order(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_first_order(self):
        self.assertEqual(max_integer([3, 1, 2]), 3)

    def test_sub_item(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "A"])

    def test_negative_item(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)
