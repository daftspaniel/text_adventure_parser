from unittest import TestCase
from text_adventure_parser.parser import Parser


class TestParser(TestCase):
    def setUp(self):
        self.parser = Parser(['go'], ['north'], {'n': 'go north'})

    def test_init(self):
        parser = Parser([1], [1, 2, 3], {})
        self.assertEqual(parser.verbs, [1])
        self.assertEqual(parser.nouns, [1, 2, 3])
        self.assertEqual(parser.shorthands, {})

    def test_parse_multi_words(self):
        result = self.parser.parse('go north')
        self.assertEqual(result.verb, 'go')
        self.assertEqual(result.noun, 'north')
        self.assertEqual(result.understood, True)

    def test_parse_single_word(self):
        result = self.parser.parse('n')
        self.assertEqual(result.verb, 'go')
        self.assertEqual(result.noun, 'north')
        self.assertEqual(result.understood, True)
