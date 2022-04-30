import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_null_input(self):
        self.assertIsNone(english_to_french(None))
        self.assertIsNone(french_to_english(None))
    
    def test_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()