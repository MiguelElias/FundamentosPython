#Escreva um programa em Python que receba três valores reais X, Y e Z,
#guarde esses valores numa tupla e verifique se esses valores podem ser os
#comprimentos dos lados de um triângulo e,
#neste caso, retorne qual o tipo de triângulo formado.
import turtle
x = int(input('Ditite o lado X do triangulo : '))
y = int(input('Ditite o lado Y do triangulo : '))
z = int(input('Ditite o lado Z do triangulo : '))
tupla = (x,y,z)


def qualifica_triangulo(tupla):
    if ( (tupla[0] != tupla[1]) and (tupla[1] != tupla[2]) and (tupla[0] != tupla[2])):
        print('Escaleno')
    elif ( (tupla[0] == tupla[1]) and (tupla[1] == tupla[2]) and (tupla[0] == tupla[2])):
        print('Equilátero')
    else:
        print('Isósceles') 

def valida_lados(tupla):
    soma=0
    maior = tupla[0]
    indice = 0
    for x in range(0,len(tupla)):
        if tupla[x]>maior:
           maior = tupla[x]
           indice = x
        if (tupla[x] == 0 ):
            print('Valor 0 não é valido !!')
    for x in range(0,len(tupla)):
        if x != indice:
            soma = soma+tupla[x]
    if(maior<soma):
        print('Medidas validas para um tringulo')
        qualifica_triangulo(tupla)        
    else:
        print('Medidas invalidas para um tringulo')
    
valida_lados(tupla)

        
        