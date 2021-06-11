from unittest import TestCase, result
from text_adventure_parser.parse_result import ParseResult


class TestParseResult(TestCase):
    def test_init(self):
        result = ParseResult('test command')
        self.assertEqual(result.understood, False)
        self.assertEqual(result.understood_verb, False)
        self.assertEqual(result.understood_noun, False)
        self.assertEqual(result.verb, '')
        self.assertEqual(result.noun, '')

    def test_str(self):
        result = ParseResult('run away')
        self.assertEqual(str(result), 'False\t\t')

    def test_happy_path(self):
        result = ParseResult('go north')
        result.verb = 'Mock Verb'
        result.noun = 'Mock Noun'
        self.assertEqual(result.explain(
        ), "Parser input was  : go north\nAfter preprocessed was  : go north\nCommand understood  : No\nVerb understood  : No\nNoun understood  : No\n")
