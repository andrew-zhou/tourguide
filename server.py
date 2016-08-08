from alias_decoder import AliasDecoder
from flask import Flask
from query_parser import QueryParser
from query_handler import QueryHandler
from settings import Settings

app = Flask(__name__)
aliases = AliasDecoder(Settings.getSetting('ALIASES_FILE_NAME')).aliases

@app.route('/alias/<string:query>', methods=['GET'])
def get_route_for_alias(query):
    handler = QueryHandler(QueryParser(query))
    return handler.handle_query(aliases)
