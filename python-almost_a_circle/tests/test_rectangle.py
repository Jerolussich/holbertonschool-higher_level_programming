import contextlib
import io
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test__init__(self):
        """init test 2 inputs"""
        self.r = Rectangle(5, 10)
        self.assertEqual(self.r.width, 5)
        self.assertEqual(self.r.height, 10)
        self.assertEqual(self.r.x, 0)
        self.assertEqual(self.r.y, 0)

    def test__init__with_5_inputs(self):
        """init test 5 inputs"""
        self.r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.height, 2)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 4)

    def test_instantiation_with_string(self):
        """Instantiation with string"""
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_instantiation_with_negatives_zero(self):
        """Instantiation with negatives/zero"""
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)

    def test_area(self):
        """return area"""
        self.r = Rectangle(5, 10)
        self.assertEqual(self.r.area(), 50)

    def test_display(self):
        """check display"""
        self.r = Rectangle(2, 3)
        captured_output = io.StringIO()
        with contextlib.redirect_stdout(captured_output):
            self.r.display()
        captured_string = captured_output.getvalue()
        self.assertEqual(captured_string, "##\n""##\n""##\n")

    def test_str_(self):
        """print string"""
        self.r = Rectangle(2, 3)
        self.assertEqual(str(self.r), "[Rectangle] (14) 0/0 -2/3")

    def test_update(self):
        """update function all inputs"""
        self.r = Rectangle(1, 2, 3, 4)
        self.r.update(1, 2, 3, 4)
        self.assertEqual(self.r.id, 1)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 3)
        self.assertEqual(self.r.x, 4)
        self.assertEqual(self.r.y, 4)

    def test_todictionary(self):
        self.r = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r.to_dictionary(), {
                         'x': 3, 'y': 4, 'id': 15, 'height': 2, 'width': 1})
