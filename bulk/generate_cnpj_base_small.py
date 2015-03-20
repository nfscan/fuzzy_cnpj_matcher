__author__ = 'paulo.rodenas'

from models.Cnpj import Cnpj


for idx in xrange(0, 100):
    from_idx = idx * 1000000
    to_idx = (idx + 1) * 1000000

    file_name = 'cnpjs_base_' + str(from_idx).zfill(7) + '.txt'
    print 'Generating from', from_idx, 'to', to_idx, file_name

    f = open(file_name, 'w')

    for cnpj_idx in xrange(from_idx, to_idx):

        cnpj_zero_padding = str(cnpj_idx).zfill(8)
        cnpj_zero_padding += '0001'
        last_two_digits = Cnpj.calculate_last_digits(cnpj_zero_padding)
        cnpj_zero_padding += ''.join(last_two_digits)

        f.write(cnpj_zero_padding + '\n')
        f.flush()

    f.close()