#13. Usando a função obtida na questão 10, desenhe n quadrados um dentro
#de outro como mostrado na figura:
import  turtle
tamanho_lado=0
quantidade =0  
while (tamanho_lado==0 ):
    tamanho_lado = int(input('Tamanho do lado: '))
while (quantidade==0 ):
    quantidade = int(input('Quantidade de quadrados: '))

def desenhar (tamanho,quantidade):
    y = 5
    z = 5
    for x in range(0,quantidade):
        
        if x == 0:
            desenha_quadrado(tamanho) 
            turtle.penup()
            turtle.goto(y,z)
            turtle.pendown()
        else:
            tamanho = tamanho -25
            desenha_quadrado(tamanho)
            turtle.penup()
            turtle.goto(y,z)
            turtle.pendown()
        y += 5
        z += 5
            
def desenha_quadrado(tam):
    for count in range(4):
        turtle.forward(tam)
        turtle.left(90)

desenhar(tamanho_lado,quantidade)