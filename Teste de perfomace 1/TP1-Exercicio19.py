#19. Dado um valor N do usuário, desenhe com a ferramenta turtle a seguinte imagem:
import turtle
n = int(input("Entre com o valor de N: "))
cont = 0
while cont <= n:
    cont = cont + 1
    turtle.color("red")
    turtle.forward(cont)
    turtle.left(90)