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
