#Entradas
valor_por_hora = float(input("Qual o valor você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalhou neste mês? "))
#Processamento
salario = horas_trabalhadas * valor_por_hora
#Saída
print("Neste mês você irá receber R${0:.2f} reais".format(salario))
