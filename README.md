# fuzzy_cnpj_matcher
A proof of concept to demonstrate the use of Fuzzy string matching for CNPJ typos.

### Purpose
The idea of this prototype is to create a way to correct a CNPJ as user types. The inspiration would be the "Did you mean?" feature we often see on Google when looking something up.

### What's a CNPJ ?
**CNPJ**, short for **Cadastro Nacional da Pessoa Jurídica** (National Registry of Legal Entities), is an identification number issued to Brazilian companies by the Secretariat of the Federal Revenue of Brazil (in Portuguese, Secretaria da Receita Federal). source: Wikipedia http://en.wikipedia.org/wiki/CNPJ

CNPJs are often used on a variety of different systems to validate whether it's a real company or not (although by only providing a CNPJ it doesn't mean it's a real company). However it's not hard hearing from customers that when they make a CNPJ typo they often need to erase the entire CNPJ and type it again as it's much harder to identify which digit is wrong.