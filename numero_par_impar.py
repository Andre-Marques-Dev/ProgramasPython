#Variáveis
p = 0
i = 0
#Entradas
numero = int(input("Informe um número: "))
#Processamento
if numero % 2 == 0:
    p = numero
else:
    i = numero
print("Par recebe {0}".format(p))
print("Ímpar recebe {0}".format(i))


