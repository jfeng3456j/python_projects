import unittest

from src.CapitalizeFirstChar import CapitalizeFirstChar


class TestCapitalizeFirstChar(unittest.TestCase):
    def setUp(self):
        self.capitalizeFirstCharacter = CapitalizeFirstChar()

    def test_emptyString(self):
        self.assertEqual("", self.capitalizeFirstCharacter.convert_char_to_cap(""))

    def test_nullString(self):
        self.assertEqual("", self.capitalizeFirstCharacter.convert_char_to_cap(None))

    def test_convert_char_to_cap(self):
        test_words = "hello there! mister"
        test_expected = "Hello There! Mister"

        self.assertEqual(test_expected, self.capitalizeFirstCharacter.convert_char_to_cap(test_words))
