from query_parser import QueryParser
from unittest import TestCase

class QueryParserTest(TestCase):
    def test_parse_empty_query(self):
        subject = QueryParser('')
        self.assertEqual(subject.query, '')
        self.assertEqual(subject.params, {})
        self.assertEqual(subject.alias, '')

    def test_parse_query_strips_whitespace(self):
        subject = QueryParser('   \t\t\n  ')
        self.assertEqual(subject.query, '')
        self.assertEqual(subject.params, {})
        self.assertEqual(subject.alias, '')

    def test_parse_query_without_params(self):
        subject = QueryParser('abcde foo bar')
        self.assertEqual(subject.query, 'abcde foo bar')
        self.assertEqual(subject.params, {})
        self.assertEqual(subject.alias, 'abcde foo bar')

    def test_parse_query_with_params(self):
        subject = QueryParser('abc  de\tfoo:bar\nfop:baz  ')
        self.assertEqual(subject.query, 'abc  de\tfoo:bar\nfop:baz')
        self.assertEqual(subject.params, {'foo': 'bar', 'fop': 'baz'})
        self.assertEqual(subject.alias, 'abc  de')
