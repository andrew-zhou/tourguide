import scripts
from flask import redirect
from query_handler import QueryHandler
from query_parser import QueryParser
from settings import Settings
from unittest import TestCase
from unittest.mock import MagicMock, patch

class QueryHandlerTest(TestCase):
    def setUp(self):
        self.aliases = {'foo': 'bar', 'script': '$fake'}

    def test_handle_backup_search_query(self):
        searchEngineMock = MagicMock(return_value='foo_')
        with patch('settings.Settings.getSetting', searchEngineMock):
            subject = QueryHandler(QueryParser('needs_search'))
            response = subject.handle_query(self.aliases)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, 'foo_needs_search')

    def test_handle_alias_query(self):
        subject = QueryHandler(QueryParser('foo'))
        response = subject.handle_query(self.aliases)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'bar')

    def test_handle_script_query(self):
        scriptMock = MagicMock()
        getAttrMock = MagicMock(return_value=scriptMock)
        subject = QueryHandler(QueryParser('script'))
        with patch('query_handler.getattr', getAttrMock):
            response = subject.handle_query(self.aliases)
            scriptMock.assert_called_with()

    def test_handle_script_query_with_params(self):
        scriptMock = MagicMock()
        getAttrMock = MagicMock(return_value=scriptMock)
        subject = QueryHandler(QueryParser('script arg1:a arg2:b'))
        with patch('query_handler.getattr', getAttrMock):
            response = subject.handle_query(self.aliases)
            scriptMock.assert_called_with(arg1='a', arg2='b')
