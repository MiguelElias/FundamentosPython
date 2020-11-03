#9. Faça uma função que desenhe o triângulo obtido na questão 7 com
#a ferramenta turtle.
import turtle


def triagulo():
    for x in range(0,4):
        for count in range(3):
            turtle.forward(100)
            turtle.left(120)
        turtle.forward(100)
triagulo()