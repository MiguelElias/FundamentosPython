#4. Escreva um programa em Python que calcule o fatorial de um dado número N
#usando um while. Use as mesmas especificações do item anterior
numero = -1
while numero < 0 :
    numero = int(input('Digite um numero válido para o calculo da fatorial: '))

def CalculaFatorial(n):
    x = n  
    fatorial = n
    multiplicador = 0
    while (x > 0):
        if x != n:
            fatorial = fatorial * x
        x -= 1
    return fatorial
       
if (numero != 0 ):
    print(f'O Fatorial de {numero} é {CalculaFatorial(numero)}')
else:
    print(f'O Fatorial de {numero} é 1')
    