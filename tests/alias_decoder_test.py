from alias_decoder import AliasDecoder
from exceptions import NotDictException, ValueNotStringException, ValueNotScriptOrUrlException
from unittest import TestCase
from unittest.mock import mock_open, patch

class AliasDecoderTest(TestCase):
    def test_array_file_throws_exception(self):
        with patch('alias_decoder.open', mock_open(read_data='[]'), create=True):
            with self.assertRaises(NotDictException):
                subject = AliasDecoder('foo')

    def test_value_not_string_file_throws_exception(self):
        with patch('alias_decoder.open', mock_open(read_data=r'{"foo": 1}'), create=True):
            with self.assertRaises(ValueNotStringException):
                subject = AliasDecoder('foo')

    def test_value_not_url_or_script_file_throws_exception(self):
        with patch('alias_decoder.open', mock_open(read_data=r'{"foo": "bar"}'), create=True):
            with self.assertRaises(ValueNotScriptOrUrlException):
                subject = AliasDecoder('foo')

    def test_proper_file_creates_aliases(self):
        with patch('alias_decoder.open', mock_open(read_data=r'{"foo": "http://bar"}'), create=True):
            subject = AliasDecoder('foo')
            self.assertEqual(subject.aliases, {'foo': 'http://bar'})
