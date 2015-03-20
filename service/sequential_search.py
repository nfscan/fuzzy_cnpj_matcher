from fuzzyset import FuzzySet

__author__ = 'paulo.rodenas'


class SequentialFuzzyCnpjMatcher:

    def __init__(self):
        self.__cnpj_bases = [
            '../bulk/cnpjs_base_00000000.txt',
            '../bulk/cnpjs_base_10000000.txt',
            '../bulk/cnpjs_base_20000000.txt',
            '../bulk/cnpjs_base_30000000.txt',
            '../bulk/cnpjs_base_40000000.txt',
            '../bulk/cnpjs_base_50000000.txt',
            '../bulk/cnpjs_base_60000000.txt',
            '../bulk/cnpjs_base_70000000.txt',
            '../bulk/cnpjs_base_80000000.txt',
            '../bulk/cnpjs_base_90000000.txt',
        ]

        self.__fuzzy_matcher = None

    def match_cnpj(self, cnpj, debug=False):
        best_matches = []

        for cnpj_base_str in self.__cnpj_bases:
            with open(cnpj_base_str) as f:
                self.__log('Searching for %s on %s' % (cnpj, cnpj_base_str), debug)
                self.__fuzzy_matcher = FuzzySet(f.read().splitlines())
                best_matches.append(self.__fuzzy_matcher.get(cnpj)[0][1])

        # Performing Fuzzy string match on the best results of each cnpj base file
        self.__fuzzy_matcher = FuzzySet(best_matches)
        return self.__fuzzy_matcher.get(cnpj_base_str)[0]

    def __log(self, msg, debug=False):
        if debug:
            print msg