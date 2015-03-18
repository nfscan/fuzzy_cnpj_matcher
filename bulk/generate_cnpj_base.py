__author__ = 'paulo.rodenas'

from models.Cnpj import Cnpj

f = open('cnpjs.txt', 'w')

for cnpj_idx in xrange(0, 999999999999):
    cnpj_zero_padding = str(cnpj_idx).zfill(12)

    last_two_digits = Cnpj.calculate_last_digits(cnpj_zero_padding)
    cnpj_zero_padding += ''.join(last_two_digits)

    assert Cnpj.validate(cnpj_zero_padding)

    f.write(cnpj_zero_padding + '\n')

f.close()