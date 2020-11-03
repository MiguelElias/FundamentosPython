#7. Utilizando a ferramenta turtle, desenhe uma série de quadrados
#um do lado do outro como indicada na figura a seguir:
import turtle
turtle.shape('turtle')

def quadrado():
    for x in range(0,4):
        for count in range(4):
            turtle.forward(100)
            turtle.left(90)
        turtle.forward(100)
quadrado()