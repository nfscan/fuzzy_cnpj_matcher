__author__ = 'paulo.rodenas'

from service.parallel_search import LocalParallelFuzzyCnpjMatcher
import unittest


class TestFuzzyMatcher(unittest.TestCase):

    def setUp(self):
        self.fuzzy_matcher = LocalParallelFuzzyCnpjMatcher(cpu_count=6)

    def test_validate(self):
        self.assertEqual(self.fuzzy_matcher.match_cnpj('10646834000196', debug=True)[1],
                         '10546844000196')
