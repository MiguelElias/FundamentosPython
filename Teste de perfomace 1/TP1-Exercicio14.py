#14. Utilizando o código 10.1 da Etapa 2, onde utilizando a função onkey do
#turtle associamos valores às setas do teclado, para este exercício associe
#as funções obtidas nas questões 10, 11 e 12 às teclas ‘q’, ‘t’ e ‘c’
#respectivamente.

import  turtle
def deseha_quadrado():
    for count in range(4):
        turtle.forward(100)
        turtle.left(90)

def triangulo():
    for count in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.forward(100)
    
def circulo():
    turtle.circle(100)
        

turtle.listen()
#10
turtle.onkey(deseha_quadrado, 'q')
#11
turtle.onkey(triangulo, 't')
#12
turtle.onkey(circulo, 'c')

