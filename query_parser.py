from re import findall, search

class QueryParser:
    PAIR_REGEXP = r'\S+:\S+'

    def __init__(self, query):
        self.query = query.strip()
        self.__parse_params_from_query()
        self.__parse_alias_from_query()

    def __parse_params_from_query(self):
        self.params = {}
        pairs = findall(self.PAIR_REGEXP, self.query)
        for pair in pairs:
            separator = pair.index(':')
            self.params[pair[:separator]] = pair[separator+1:]

    def __parse_alias_from_query(self):
        self.alias = self.query
        first_pair = search(self.PAIR_REGEXP, self.query)
        if first_pair:
            self.alias = self.query[:first_pair.start()].strip()
