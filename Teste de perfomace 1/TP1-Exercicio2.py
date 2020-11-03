#2. Faça uma função em Python que receba do usuário a idade de uma pessoa em anos,
# meses e dias e retorne essa idade expressa em dias.
#Considere que todos os anos têm 365 dias.

anos = 0
while anos <= 0:
    anos = int(input('Digite quantos anos você tem: '))
meses = int(input('Digite quantos meses você tem: '))
dias = int(input('Digite quantos dias você tem: '))

def CalculaDias(ano,mes,dia):
    return (ano*365) + (mes*30)+dia
    
    
print(f'A quatidade de dias é {CalculaDias(anos,meses,dias)}')