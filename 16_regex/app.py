import re

string = 'Este é um teste de expressões reguladores.'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'pau', string))