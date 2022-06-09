"""
Test suite.
"""

import unittest

import triepy

class TestTriepy(unittest.TestCase):

    def test_triepy(self):
        trie = triepy.Trie()
        trie["key"] = 1
        self.assertEqual(trie["key"], 1)


if __name__ == "__main__":
    unittest.main()
