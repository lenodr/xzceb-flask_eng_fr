import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_null_input_english(self):
        self.assertIsNone(english_to_french(None))

    def test_english_to_french_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
    def test_null_input_french(self):
        self.assertIsNone(french_to_english(None))
    
    def test_french_to_english_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()