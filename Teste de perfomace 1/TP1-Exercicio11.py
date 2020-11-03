#11. Faça uma função no Python que, utilizando a ferramenta turtle,
#desenhe um triângulo de lado N.
import  turtle

tamanho_lado = 0
while (tamanho_lado==0 ):
    tamanho_lado = int(input('Tamanho do lado: '))

def triangulo(lado):
    for count in range(3):
        turtle.forward(lado)
        turtle.left(120)
    turtle.forward(lado)
triangulo(tamanho_lado)
    