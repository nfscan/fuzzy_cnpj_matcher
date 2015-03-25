import time
from fuzzyset import FuzzySet

__author__ = 'paulo.rodenas'


class SequentialFuzzyCnpjMatcher:
    """
    Class that performs fuzzy string matching on CNPJs sequentially. For small
    fuzzyset this class is the easiest way to get started. However if you going
    for a large fuzzyset we strongly recommend using LocalParallelFuzzyCnpjMatcher
     instead.
    """

    def __init__(self):
        """
        Default constructor
        :return: a SequentialFuzzyCnpjMatcher instance
        """
        self.__cnpj_bases = []

        for x in xrange(0, 100):
            idx = x * 1000000
            self.__cnpj_bases.append('../bulk/cnpjs_base_' + str(idx).zfill(7) +
                                     '.txt')

        self.__fuzzy_matcher = None

    def match_cnpj(self, cnpj, debug=False):
        """
        Search the closest valid CNPJ given a invalid one
        :param cnpj: a invalid CNPJ
        :param debug: whether you want to see debugging logs or not
        :return: a list of the most similar valid CNPJs to the one you've provided
        """
        best_matches = []

        for cnpj_base_str in self.__cnpj_bases:
            with open(cnpj_base_str) as f:
                # temp variables
                start_time = time.time()

                # Searching
                self.__log('Searching for %s on %s' % (cnpj, cnpj_base_str), debug)
                self.__fuzzy_matcher = FuzzySet(f.read().splitlines())

                match = self.__fuzzy_matcher.get(cnpj)
                elapsed_time = time.time() - start_time

                self.__log('Best match for this file is %s and it took %d seconds'
                           % (match, elapsed_time), debug)
                # Appending to the best matches so far
                if not match is None:
                    for m in match:
                        best_matches.append(m[1])

        # Performing Fuzzy string match on the best results of each cnpj base file
        self.__fuzzy_matcher = FuzzySet(best_matches)
        return self.__fuzzy_matcher.get(cnpj)[0]

    def __log(self, msg, debug=False):
        """
        Prints a message to console depending on debug variable
        :param msg: a message string
        :param debug: a boolean value
        :return:
        """
        if debug:
            print msg