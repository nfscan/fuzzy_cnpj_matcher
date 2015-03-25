import time
from fuzzyset import FuzzySet
import pp
import psutil

__author__ = 'paulo.rodenas'


class BaseParallelFuzzyCnpjMatcher(object):

    def __init__(self):
        self.cnpj_bases = []

        for x in xrange(0, 10):
            idx = x * 1000000
            self.cnpj_bases.append('../bulk/cnpjs_base_' + str(idx).zfill(7) +
                                     '.txt')

        self.fuzzy_matcher = None


class LocalParallelFuzzyCnpjMatcher(BaseParallelFuzzyCnpjMatcher):

    def __init__(self, cpu_count="autodetect"):
        super(LocalParallelFuzzyCnpjMatcher, self).__init__()
        self.__job_server = pp.Server(ncpus=cpu_count)

    def match_cnpj(self, cnpj, debug=False):
        best_matches = []

        # temp variables
        start_time = time.time()

        jobs = [(
                    cnpj_base_str,
                    self.__job_server.submit(
                        fuzzy_cnpj_search,
                        (cnpj_base_str, cnpj, debug,),
                        (log, ),
                        ("from fuzzyset import FuzzySet", "time")
                    )) for cnpj_base_str in self.cnpj_bases]

        for cnpj_base_str, job in jobs:
            print "Results", cnpj_base_str, "is", job()

        elapsed_time = time.time() - start_time

        log('Parallel processes took %d seconds to finish' % elapsed_time, debug)

        # Performing Fuzzy string match on the best results of each cnpj base file
        self.fuzzy_matcher = FuzzySet(best_matches)
        return self.fuzzy_matcher.get(cnpj)[0]


def fuzzy_cnpj_search(cnpj_base_str, cnpj, debug=False):
    best_matches = []
    with open(cnpj_base_str) as f:
        # temp variables
        start_time = time.time()

        # Searching
        log('Searching for %s on %s' % (cnpj, cnpj_base_str), debug)
        fuzzy_matcher = FuzzySet(f.read().splitlines())

        match = fuzzy_matcher.get(cnpj)
        elapsed_time = time.time() - start_time

        log('Best match for this file is %s and it took %d seconds'
                   % (match, elapsed_time), debug)
        # Appending to the best matches so far
        if not match is None:
            for m in match:
                best_matches.append(m[1])
        return best_matches


def log(msg, debug=False):
        if debug:
            print msg