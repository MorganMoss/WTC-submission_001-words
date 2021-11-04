import unittest
from word_processor import *

class TestWordProcessor(unittest.TestCase):
    def test_convert_to_word_list(self):
        text = "I am bob, your uncle."
        self.assertEqual(
                convert_to_word_list(text), 
                ["i", "am", "bob", "your", "uncle"]
            )