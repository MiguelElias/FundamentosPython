#20. Baseando no código criado na questão anterior, crie uma função na qual dado um N
#obtido através do usuário, sua tartaruga gire 90 + N graus. Teste para 1, 4 e 10 para obter as figuras a seguir.
import turtle
numero = int(input('Digite um numero:'))
def desehar(n):
    color = ('red')
    turtle.shape('turtle')
    turtle.speed('fastest')
    for x in range(360):
        turtle.forward(x)
        turtle.left(90+n)
desehar(numero)