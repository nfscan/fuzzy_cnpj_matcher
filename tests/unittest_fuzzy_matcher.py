__author__ = 'paulo.rodenas'

from fuzzyset import FuzzySet
import unittest


class TestFuzzyMatcher(unittest.TestCase):

    def setUp(self):
        with open('../bulk/cnpjs.txt') as f:
            self.fuzzy_set = f.read().splitlines()
            self.fuzzy_matcher = FuzzySet(self.fuzzy_set)

    def test_validate(self):
        self.assertEqual(self.fuzzy_matcher.get('06389497000195')[0][1],
                         '04389697000195')
        self.assertEqual(self.fuzzy_matcher.get('15574828000190')[0][1],
                         '15575829000190')
        self.assertEqual(self.fuzzy_matcher.get('15911974000144')[0][1],
                         '15922975000144')
        self.assertEqual(self.fuzzy_matcher.get('12919223000129')[0][1],
                         '12291923000129')
        self.assertEqual(self.fuzzy_matcher.get('557135900011')[0][1],
                         '55713579000121')
        self.assertEqual(self.fuzzy_matcher.get('40194766000116')[0][1],
                         '49794166000116')

        #'49794166000116'
        print self.fuzzy_matcher.get('40194766000116')[0][1]

