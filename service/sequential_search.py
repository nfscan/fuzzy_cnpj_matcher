import time
from fuzzyset import FuzzySet

__author__ = 'paulo.rodenas'


class SequentialFuzzyCnpjMatcher:

    def __init__(self):
        self.__cnpj_bases = [
            '../bulk/cnpjs_base_0000000.txt',
            '../bulk/cnpjs_base_1000000.txt',
            '../bulk/cnpjs_base_2000000.txt',
            '../bulk/cnpjs_base_3000000.txt',
            '../bulk/cnpjs_base_4000000.txt',
            '../bulk/cnpjs_base_5000000.txt',
            '../bulk/cnpjs_base_6000000.txt',
            '../bulk/cnpjs_base_7000000.txt',
            '../bulk/cnpjs_base_8000000.txt',
            '../bulk/cnpjs_base_9000000.txt',
        ]

        self.__fuzzy_matcher = None

    def match_cnpj(self, cnpj, debug=False):
        best_matches = []

        for cnpj_base_str in self.__cnpj_bases:
            with open(cnpj_base_str) as f:
                # temp variables
                match = None
                start_time = time.time()

                # Searching
                self.__log('Searching for %s on %s' % (cnpj, cnpj_base_str), debug)
                self.__fuzzy_matcher = FuzzySet(f.read().splitlines())

                match = self.__fuzzy_matcher.get(cnpj)
                elapsed_time = time.time() - start_time

                self.__log('Best match for this file is %s and it took %d seconds' % (match, elapsed_time), debug)
                # Appending to the best matches so far
                if not match is None:
                    for m in match:
                        best_matches.append(m[1])

        # Performing Fuzzy string match on the best results of each cnpj base file
        self.__fuzzy_matcher = FuzzySet(best_matches)
        return self.__fuzzy_matcher.get(cnpj_base_str)[0]

    def __log(self, msg, debug=False):
        if debug:
            print msg