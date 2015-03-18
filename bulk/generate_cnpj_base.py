__author__ = 'paulo.rodenas'

for cnpj_idx in range(0, 999999999999):
    cnpj_zero_padding = str(cnpj_idx).zfill(12)
    print cnpj_zero_padding