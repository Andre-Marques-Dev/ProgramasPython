"""
Listas

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença de
serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Phyton:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

# Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

"""

"""
Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adcicionar 1 elemento por vez

# exemplo:
lista1.append(12, 34, 56) # erro

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 5, 1]) # coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # coloca cada elemento da lista como valor adcional à lista
print(lista1)

# podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'novo valor')
print(lista1)

# Podemos facilmente juntar duas listas
lista1 = lista1 + lista2
print(lista1)

# Podemos facilmente inverter uma lista utilizando reverse
# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice serão colocados para a esquerda.
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos de uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['C', 'r', 'u', 'z', 'e', 'i', 'r', 'o', ' ', 'E', 's', 'p', 'o', 'r', 't', 'e']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek Univesity')
