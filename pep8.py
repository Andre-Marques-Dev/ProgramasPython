"""
PEP8 - Python Enhancement proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

Aideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - utilize camel case para nomes de classes;

class Calculadora:
pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação! (Não use tab)

if 'a' in 'banana':
    print("tem")

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

class Classe:
    pass


class Outra:
    pass

[5] - Imports

- Imports devem sempre ser feitos em linhas separadas;

#Import errado

import sys, os

#Import certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocado no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes
de constantes e variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrunção com uma nova linha
"""
import this



