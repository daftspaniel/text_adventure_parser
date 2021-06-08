from unittest import TestCase, result
from text_adventure_parser.parse_result import ParseResult


class TestParseResult(TestCase):
    def test_init(self):
        result = ParseResult()
        self.assertEqual(result.understood, False)
        self.assertEqual(result.understood_verb, False)
        self.assertEqual(result.understood_noun, False)
        self.assertEqual(result.verb, '')
        self.assertEqual(result.noun, '')
    def test_str(self):
        result = ParseResult()
        self.assertEqual(str(result),'False\t\t')