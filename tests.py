import unittest
from fibo import text_analysis

class TestTextAnalysis(unittest.TestCase):
    def test_basic_text(self):
        text = "Hello world! This is a test. There are 2 sentences and 3 numbers: 1, 2, and 3."
        result = text_analysis(text)
        expected = {
            'num_words': 14,
            'num_sentences': 3,
            'num_unique_words': 12,
            'num_numbers': 4
        }
        self.assertEqual(result, expected)
    
    def test_empty_text(self):
        text = ""
        result = text_analysis(text)
        expected = {
            'num_words': 0,
            'num_sentences': 0,
            'num_unique_words': 0,
            'num_numbers': 0
        }
        self.assertEqual(result, expected)
    
    def test_text_without_numbers(self):
        text = "This is a test without numbers."
        result = text_analysis(text)
        expected = {
            'num_words': 6,
            'num_sentences': 1,
            'num_unique_words': 6,
            'num_numbers': 0
        }
        self.assertEqual(result, expected)
    
    def test_text_with_only_numbers(self):
        text = "123 456 789"
        result = text_analysis(text)
        expected = {
            'num_words': 3,
            'num_sentences': 1,
            'num_unique_words': 3,
            'num_numbers': 3
        }
        self.assertEqual(result, expected)

def check_true(_condition: float) -> bool:
    if _condition < 10:
        return False
    else:
        return True
    

def check_true(_condition: str) -> bool:
    if _condition == "bad answer":
        return True
    else:
        return False

if __name__ == '__main__':
    unittest.main()

# 1