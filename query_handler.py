import scripts
from flask import redirect
from query_parser import QueryParser
from settings import Settings

class QueryHandler:
    def __init__(self, query_parser):
        self.query_parser = query_parser

    def handle_query(self, aliases):
        if self.query_parser.alias not in aliases:
            # Need to put this as a search term instead
            return self.__backup_search()
        route = aliases[self.query_parser.alias]
        # Routes that are prefixed with $ refer to custom methods that
        # return a redirect object
        if route[0] == '$':
            return self.__run_script(route[1:])
        else:
            return redirect(route)

    def __run_script(self, script_name):
        return getattr(scripts, script_name)(**self.query_parser.params)

    def __backup_search(self):
        return redirect('{0}{1}'.format(Settings.getSetting('BACKUP_SEARCH_BASE'), self.query_parser.query))
