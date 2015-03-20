__author__ = 'paulo.rodenas'

from service.sequential_search import SequentialFuzzyCnpjMatcher
import unittest


class TestFuzzyMatcher(unittest.TestCase):

    def setUp(self):
        self.fuzzy_matcher = SequentialFuzzyCnpjMatcher()

    def test_validate(self):
        self.assertEqual(self.fuzzy_matcher.match_cnpj('06389497000195', debug=True)[0][1],
                         '04389697000195')
        self.assertEqual(self.fuzzy_matcher.match_cnpj('15574828000190', debug=True)[0][1],
                         '15575829000190')
        self.assertEqual(self.fuzzy_matcher.match_cnpj('15911974000144', debug=True)[0][1],
                         '15922975000144')
        self.assertEqual(self.fuzzy_matcher.match_cnpj('12919223000129', debug=True)[0][1],
                         '12291923000129')
        self.assertEqual(self.fuzzy_matcher.match_cnpj('557135900011', debug=True)[0][1],
                         '55713579000121')
        self.assertEqual(self.fuzzy_matcher.match_cnpj('40194766000116', debug=True)[0][1],
                         '49794166000116')

