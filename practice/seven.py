import capitalize
import unittest

class TestCapitalize(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        res = capitalize.capitalize(text)
        self.assertEqual(res, 'Python')
    
    def test_many_words(self):
        text = 'this is a test sentence'
        res = capitalize.capitalize(text)
        self.assertEqual(res, 'This Is A Test Sentence')

if __name__ == '__main__':
    unittest.main()