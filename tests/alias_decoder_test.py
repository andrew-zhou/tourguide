from unittest import TestCase
from unittest.mock import mock_open, patch
from alias_decoder import AliasDecoder
from exceptions import NotDictException, ValueNotStringException

class AliasDecoderTest(TestCase):
    def test_array_file_throws_exception(self):
        with patch('alias_decoder.open', mock_open(read_data='[]'), create=True) as _:
            with self.assertRaises(NotDictException):
                subject = AliasDecoder('foo')

    def test_value_not_string_file_throws_exception(self):
        with patch('alias_decoder.open', mock_open(read_data=r'{"foo": 1}'), create=True) as _:
            with self.assertRaises(ValueNotStringException):
                subject = AliasDecoder('foo')

    def test_proper_file_creates_aliases(self):
        with patch('alias_decoder.open', mock_open(read_data=r'{"foo": "bar"}'), create=True) as _:
            subject = AliasDecoder('foo')
            self.assertEqual(subject.aliases, {'foo': 'bar'})
