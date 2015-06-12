__author__ = 'paulo.rodenas'

import unittest
from models.Cnpj import *


class TestCnpjValidation(unittest.TestCase):

    def test_validate(self):
        # Valid ones
        self.assertTrue(Cnpj.validate('25.996.438/0001-00'))
        self.assertTrue(Cnpj.validate('29.759.260/0001-27'))
        self.assertTrue(Cnpj.validate('73.821.424/0001-90'))

        # Invalid ones
        self.assertFalse(Cnpj.validate('25.996.438/0001-01'))
        self.assertFalse(Cnpj.validate('29.759.260/0001-22'))
        self.assertFalse(Cnpj.validate('73.821.424/0001-94'))

        # Generated ones
        self.assertTrue(Cnpj.validate(Cnpj.generate_valid_cnpj()))
        self.assertTrue(Cnpj.validate(Cnpj.generate_valid_cnpj()))
        self.assertTrue(Cnpj.validate(Cnpj.generate_valid_cnpj()))
