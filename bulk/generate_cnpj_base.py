__author__ = 'paulo.rodenas'

from models.Cnpj import Cnpj

f = open('cnpjs_base_10000000.txt', 'w')

for cnpj_idx in xrange(0, 10000000):
    # cnpj_zero_padding = str(cnpj_idx).zfill(12)
    # last_two_digits = Cnpj.calculate_last_digits(cnpj_zero_padding)
    # cnpj_zero_padding += ''.join(last_two_digits)

    cnpj_zero_padding = str(cnpj_idx).zfill(8)
    cnpj_zero_padding += '0001'
    last_two_digits = Cnpj.calculate_last_digits(cnpj_zero_padding)
    cnpj_zero_padding += ''.join(last_two_digits)

    # cnpj_zero_padding = Cnpj.generate_valid_cnpj_with_no_branch()

    assert Cnpj.validate(cnpj_zero_padding)

    f.write(cnpj_zero_padding + '\n')

f.close()