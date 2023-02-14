import unittest
import json

from models.base import Base
from models.rectangle import Rectangle


class Testbase(unittest.TestCase):

    def test_no_args(self, *args):
        """test no args"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_args(self):
        """test given args"""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_tojsonstring(self):
        """test output given string"""
        data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        result = Base.to_json_string(data)
        expected = json.dumps(data)
        self.assertEqual(result, expected)

    def test_tojsonstring2(self):
        """test output no string given"""
        data = None
        result = Base.to_json_string(data)
        expected = "[]"
        self.assertEqual(result, expected)

    def test_from_jsonstring(self):
        """test output given string"""
        data = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        input = Rectangle.to_json_string(data)
        result = Base.from_json_string(input)
        expected = json.loads(input)
        self.assertEqual(result, expected)

    def test_from_jsonstring2(self):
        """test output no string given"""
        data = None
        result = []
        expected = []
        self.assertEqual(result, expected)
