__author__ = 'paulo.rodenas'

from service.sequential_search import SequentialFuzzyCnpjMatcher
import unittest


class TestFuzzyMatcher(unittest.TestCase):

    def setUp(self):
        self.fuzzy_matcher = SequentialFuzzyCnpjMatcher()

    def test_validate(self):
        self.assertEqual(self.fuzzy_matcher.match_cnpj('10646834000196', debug=True)[1],
                         '10546844000196')
