from unittest import TestCase
from text_adventure_parser.parser import Parser


class TestParser(TestCase):
    def setUp(self):
        self.parser = Parser(['go', 'look'], ['inventory', 'north'], {
                             'n': 'go north', 'i': 'look inventory'})

    def test_init(self):
        parser = Parser([1], [1, 2, 3], {})
        self.assertEqual(parser.verbs, [1])
        self.assertEqual(parser.nouns, [1, 2, 3])
        self.assertEqual(parser.shorthands, {})
    
    def test_known_verbs(self):
        self.assertEqual(self.parser.get_known_verbs(), ['go', 'look'])

    def test_parse_empty_string(self):
        result = self.parser.parse('')
        self.assertEqual(result.understood, False)
        self.assertEqual(result.understood_verb, False)
        self.assertEqual(result.understood_noun, False)
        self.assertEqual(result.verb, '')
        self.assertEqual(result.noun, '')

    def test_parse_single_word_shorthand(self):
        result = self.parser.parse('n')
        self.assertEqual(result.verb, 'go')
        self.assertEqual(result.noun, 'north')
        self.assertEqual(result.understood, True)

    def test_parse_single_word_shorthand_and_command(self):
        result = self.parser.parse('i')
        self.assertEqual(result.verb, 'look')
        self.assertEqual(result.noun, 'inventory')
        self.assertEqual(result.understood, True)

    def test_parse_unknown_verb(self):
        result = self.parser.parse('dance north')
        self.assertEqual(result.verb, 'dance')
        self.assertEqual(result.noun, 'north')
        self.assertEqual(result.understood, False)
        self.assertEqual(result.understood_noun, True)
        self.assertEqual(result.understood_verb, False)

    def test_parse_unknown_noun(self):
        result = self.parser.parse('go monkey')
        self.assertEqual(result.verb, 'go')
        self.assertEqual(result.noun, 'monkey')
        self.assertEqual(result.understood, False)
        self.assertEqual(result.understood_noun, False)
        self.assertEqual(result.understood_verb, True)
