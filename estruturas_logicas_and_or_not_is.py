"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not,

Operadores binários:
    - and, or, is

Regras de funcionamento:

para o "and", ambos os valores precisam ser True
para o "or", um ou outro valor precisa ser True
para o "not", o valor do Booleano é invertido, ou seja, se for True vira False, se for False vira True
para o "is", o valor é comparado com um segundo
"""
ativo = False
logado = False

if ativo or logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor cheque seu e-mail")
