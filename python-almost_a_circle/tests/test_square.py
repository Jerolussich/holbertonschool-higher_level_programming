import unittest

from models.square import Square


class Testsquare(unittest.TestCase):

    def setUp(self):
        # Create an instance of Square to test with
        self.s = Square(5)

    def test_init(self):
        """init test"""
        self.assertEqual(self.s.size, 5)
        self.assertEqual(self.s.x, 0)
        self.assertEqual(self.s.y, 0)

    def test_str(self):
        """str print test"""
        self.assertEqual(
            str(self.s), "[Square] (27) 0/0 - 5")

    def test_update(self):
        """update function all inputs"""
        self.s.update(1, 2, 3, 4)
        self.assertEqual(self.s.id, 1)
        self.assertEqual(self.s.width, 2)
        self.assertEqual(self.s.x, 3)
        self.assertEqual(self.s.y, 4)

    def test_instantiation_with_string(self):
        """Instantiation with string"""
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "2")
        self.assertRaises(TypeError, Square, 1, 2, "3")

    def test_instantiation_with_negatives_zero(self):
        """Instantiation with negatives/zero"""
        self.assertRaises(ValueError, Square, -1, 2)
        self.assertRaises(ValueError, Square, 1, -2)
        self.assertRaises(ValueError, Square, 0, 2)
        self.assertRaises(ValueError, Square, 1, 2, -3)
