from re import findall, search

class QueryParser:
    PAIR_REGEXP = r'\S+:\S+'

    def __init__(self, query):
        self.query = query.strip()
        self.parse_params_from_query()
        self.parse_alias_from_query()

    def parse_params_from_query(self):
        self.params = {}
        pairs = findall(self.PAIR_REGEXP, self.query)
        for pair in pairs:
            separator = pair.index(':')
            self.params[pair[:separator]] = pair[separator+1:]

    def parse_alias_from_query(self):
        self.alias = self.query
        first_pair = search(self.PAIR_REGEXP, self.query)
        if first_pair:
            self.alias = self.query[:first_pair.start()].strip()
