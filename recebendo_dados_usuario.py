"""
Recebendo dados do usuário

input() -> todo dado recebido via input é do tipo string

Em Python, string  é tudo  que estiver entre:
- Aspas simples;
- Aspas dulpas:
- Aspas simples triplas:
- Aspas dulpas triplas;

Exemplos
- Aspas simples -> 'Andreé Marques'
- Aspas dulpas -> "André Marques"
- Aspas simples triplas -> '''André Marques'''
"""
# - Aspas dulpas triplas -> """André Marques"""

# Entrada de dados
# print("Qual o seu nome? ")
# nome = input() # input -> Entrada

nome = input("Qual o seu nome?" )

# Exemplo de print 'antigo' 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print 'moderno' 3.x
# print("Seja bem-vindo(a) {0}" .format(nome))

# Exemplo de print 'mais atual' 3.7
print(f"Seja bem-vindo(a) {nome}")

# print("Qual a sua idade? "),
# idade = input()

idade = input("Qual a sua idade?" )

# print("Qual o seu time do coração? ")
# time = input()

time = input("Qual é o seu time do coração?" )

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print("O %s tem %s anos e seu time do coração é %s " %  (nome, idade, time))

# Exemplo de print 'moderno' 3.x
# print("O {0} tem {1} anos e seu time do coração é {2}" .format(nome, idade, time))

# Exemplo de print 'mais atual' 3.7
print(f"O {nome} tem {idade} anos e seu time do coração é {time}")

"""
# int(idade) => cast

cast é a "conversão" de um tipo de dado em outro.
"""

print(f"O {nome} nasceu em {2021 - int(idade)}")