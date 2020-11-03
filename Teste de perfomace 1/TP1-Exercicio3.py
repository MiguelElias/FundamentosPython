#3.Escreva uma função em Python que calcule o fatorial de um dado número N 
#usando um for. O fatorial de N=0 é um. O fatorial de N é
#(para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1.Por exemplo, para
#N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120.
# Se N for negativo, exiba uma mensagem indicando que não é possível calcular
# seu fatorial.
numero = -1 
while numero < 0:
    numero = int(input('Digite um numero válido para o calculo da fatorial: '))


def CalculaFatorial(n):
    for x in range (n,0,-1):
        if x == n :
            resultado=n
        else:
            resultado = resultado*x
    return resultado      

if numero != 0:
    print(f'O Fatorial de {numero} é {CalculaFatorial(numero)}')
else:
    print(f'O Fatorial de {numero} é 1')
    