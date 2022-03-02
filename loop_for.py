"""
Loop for
Loop -> Estrutura de repetição
For  -> É uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
  //execução do loop
}

Python

for intem in iteravel:
  //execução do loop

utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
  nome = 'Geek University'
- Lista
  lista = [1, 3, 5, 7, 9]
- Range
  numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)
#Exemplode for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)
OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - não

for numero in range(1, 10):
    print(numero)

Enumerates:

for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_).

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Cruzeiro Esporte'
for letra in nome:
    print(letra, end='')
"""
#original: U+1F60D
# Modificado: U0001F60D

for num in range(1, 11):
    print('\U0001F60D' * num)






