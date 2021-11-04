import unittest
from word_processor import *

class TestWordProcessor(unittest.TestCase):
    """
    note that the delimeter is following the instructions in step 1,
    thus '!' and '-' etc are not delimeters. Only the ones specified are.
    """

    def test_convert_to_word_list(self):
        text = "I am Bob, your uncle."
        self.assertEqual(
                convert_to_word_list(text), 
                ["i", "am", "bob", "your", "uncle"]
            )
        self.assertEqual(
                convert_to_word_list(''), 
                []
            )
    
    def test_words_longer_than(self):
        text = "Leave me alone, Bob. You're not my uncle are you?"
        self.assertEqual(
                words_longer_than(4, text), 
                ["leave", "alone", "you're", "uncle"]
            )
        self.assertEqual(
                words_longer_than(3, ''), 
                []
            )
        self.assertEqual(
                words_longer_than(0, text), 
                ["leave", "me", "alone", "bob", "you're",
                 "not", "my", "uncle", "are", "you"]
            )


    def test_words_lengths_map(self):
        text = "Seriously, stop following me - not my uncle!"
        self.assertEqual(
            words_lengths_map(text),
            {9:2,6:1,4:1,3:1,2:2,1:1}
            )
        self.assertEqual(
            words_lengths_map(''),
            {}
            )


    def test_letters_count_map(self):
        text = "Yes I am, of course!"
        self.assertEqual(
                letters_count_map(''), 
                {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
                 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 
                 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 
                 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 
                 'y': 0, 'z': 0}
            )
        self.assertEqual(
                letters_count_map(text), 
                {'a': 1, 'b': 0, 'c': 1, 'd': 0, 'e': 2, 'f': 1,
                 'g': 0, 'h': 0, 'i': 1, 'j': 0, 'k': 0, 'l': 0, 
                 'm': 1, 'n': 0, 'o': 2, 'p': 0, 'q': 0, 'r': 1, 
                 's': 2, 't': 0, 'u': 1, 'v': 0, 'w': 0, 'x': 0, 
                 'y': 1, 'z': 0}
            )


    def test_most_used_character(self):
        text = "I'm calling the cops if you don't leave me alone"
        self.assertEqual(
                    most_used_character(text),
                    'e'
                )
        self.assertEqual(
                    most_used_character(''),
                    None
                )
        

    def test_leng(self):
        text = "Fine! I'll go..."
        self.assertEqual(leng(text), len(text))
        self.assertEqual(leng(''), len(''))

    
    def test_lower(self):
        text = "Thank GoOdNEss!"
        self.assertEqual(lower(text),text.lower())
        self.assertEqual(lower(''),''.lower())

