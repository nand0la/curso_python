"""
    são padrões utilizados para identificar 
    eterminadas ocorrências em uma cadeias de 
    caracteres.
"""
import re

string = """
    Às vezes, é fácil sorrir
Às vezes, só fecha a cara
Às vezes, é só dormir
Às vezes, não melhora

Às vezes, é fácil ouvir
Às vezes, é gritaria
Às vezes, é um poço sem fim
Às vezes, é uma escada

Calma, vai passar
Espera a tempestade clarear
Os maremotos de química surgem
Bagunçam tua cabeça a todo vapor

Calma, vai passar
Espera a tempestade clarear
Os travesseiros derretem à noite
Todos que cobram você, não sabem a dor

Às vezes, esconde de si
Às vezes, dá a cara a tapa
Às vezes, não dá pra fugir
Às vezes, tu só viaja

Calma, vai passar
Espera a tempestade clarear
Os maremotos de química surgem
Bagunçam tua cabeça a todo vapor

Calma, vai passar
Espera a tempestade clarear
Os travesseiros derretem à noite
Todos que cobram você, não entendem a dor

O eu de dentro sempre fica enterrado
Pra conhecer, você precisa cavar
Nossas sementes sempre ficam isoladas
Pra conhecer, você precisa plantar

Nossos espinhos sempre ficam apontados
É proteção pra não se decepcionar
Os nossos medos são os nossos papagaios
Pesam os ombros e repetem mantras infernais

Calma, vai passar
Espera a tempestade clarear
Os maremotos de química surgem
Bagunçam tua cabeça a todo vapor

Calma, vai passar
Espera a tempestade clarear
Os travesseiros derretem à noite
Todos que cobram você, não sentem dor

123.321.321-21

O eu de dentro sempre fica enterrado
Pra conhecer, você precisa cavar
Nossas sementes sempre ficam isoladas
Pra conhecer, você precisa plantar

email@gmail.com
email2@gmail.com


Nossos espinhos sempre ficam afiados
É proteção pra não se decepcionar
Os nossos medos são os nossos papagaios
Pesam os ombros e repetem mantras infernais
"""

"""
print(re.search(r'teste', string))  # acha o indice de determinada palavra
print(re.findall(r'teste', string))  # acha o indice de determinadas palavras
print(re.sub(r'teste', 'pau', string))  # subsitui palavras
"""

print(re.findall(r'Nossos|.onhecer', string))
print(re.findall(r'[0-9][0-9][0-9].[0-9][0-9][0-9].[0-9][0-9][0-9]-[0-9][0-9]', string))
print(re.findall(r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}', string))
print(re.findall(r'[a-zA-Z0-9]+@gmail.com', string))