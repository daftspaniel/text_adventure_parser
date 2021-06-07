from unittest import TestCase
from text_adventure_parser.parse_result import ParseResult


class TestParseResult(TestCase):
    def test_init(self):
        result = ParseResult()
        self.assertEqual(result.understood, False)
        self.assertEqual(result.verb, '')
        self.assertEqual(result.noun, '')
