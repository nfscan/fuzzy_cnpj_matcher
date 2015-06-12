# fuzzy_cnpj_matcher
[![Build Status](https://travis-ci.org/nfscan/fuzzy_cnpj_matcher.svg)](https://travis-ci.org/nfscan/fuzzy_cnpj_matcher)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/nfscan/fuzzy_cnpj_matcher/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/nfscan/fuzzy_cnpj_matcher.svg)](https://github.com/nfscan/fuzzy_cnpj_matcher/network)
[![Coverage Status](https://coveralls.io/repos/nfscan/fuzzy_cnpj_matcher/badge.svg)](https://coveralls.io/r/nfscan/fuzzy_cnpj_matcher)

A proof of concept to demonstrate the use of Fuzzy string matching for CNPJ typos.

### Purpose
The idea of this prototype is to create a way to correct a CNPJ as user types it. The inspiration would be the "Did you mean?" feature we often see on Google when looking something up.

![](https://raw.githubusercontent.com/pauloubuntu/fuzzy_cnpj_matcher/master/github_image/example.png)

### What's a CNPJ ?
**CNPJ**, short for **Cadastro Nacional da Pessoa Jurídica** (National Registry of Legal Entities), is an identification number issued to Brazilian companies by the Secretariat of the Federal Revenue of Brazil (in Portuguese, Secretaria da Receita Federal). source: Wikipedia http://en.wikipedia.org/wiki/CNPJ

CNPJs are often used on a variety of systems to validate whether it's a real company or not (although by only providing a CNPJ it doesn't mean it's a real company). However it's not hard hearing from customers that when they make a CNPJ typo they often need to clean the entire CNPJ and type it again as it's much harder to identify which digit is wrong.

### Dependencies

```Shell
# Parallel Python   - http://www.parallelpython.com/
pip install pp

# Fuzzyset          - https://github.com/axiak/fuzzyset
easy_install fuzzyset
```



