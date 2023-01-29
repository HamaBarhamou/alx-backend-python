#!/usr/bin/env python3
"""A github org client
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
            [{"a": 1}, ("a",), 1,],
            [{"a": {"b": 2}}, ("a",), {"b": 2},],
            [{"a": {"b": 2}}, ("a", "b"), 2,],
        ])
    def test_access_nested_map(self, nested_map, path, result):
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
            [{}, ("a",), KeyError,],
            [{"a": 1}, ("a", "b"), KeyError,],
        ])
    def test_access_nested_map_exception(self, nested_map, path, result):
        with self.assertRaises(KeyError) as e:
            self.assertEqual(access_nested_map(nested_map, path), e.exception)
