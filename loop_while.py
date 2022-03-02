"""
Loop while

Forma geral

while expressao_booleana:
    //execuçaõ do loop

o bloco do while será repetida enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo 1:
num = 5
num < 5 -> False

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# OBS: Em um loop while, é importante  que cuidemos do critério de parada, para não causar loop infinito.
"""
# Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
