from unittest import TestCase
from text_adventure_parser.text_util import yes_no, list_to_text


class TestTextUtil(TestCase):

    def test_yes_no(self):
        self.assertEqual(yes_no(True), 'Yes')
        self.assertEqual(yes_no(False), 'No')

    def test_list_to_text_empty(self):
        result = list_to_text([])
        self.assertEqual(result, 'Nothing.')

    def test_list_to_text_single(self):
        result = list_to_text(['owl'])
        self.assertEqual(result, 'Owl.')

    def test_list_to_text_two(self):
        result = list_to_text(['owl', 'duck'])
        self.assertEqual(result, 'Duck and owl.')

    def test_list_to_text_three(self):
        result = list_to_text(['goose', 'owl', 'duck'])
        self.assertEqual(result, 'Duck, goose and owl.')
