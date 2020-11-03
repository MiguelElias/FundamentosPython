#10. Faça uma função no Python que, utilizando a ferramenta turtle,
#desenhe um quadrado de lado N.
import  turtle
tamanho_lado=0
while (tamanho_lado==0 ):
    tamanho_lado = int(input('Tamanho do lado: '))

def deseha_quadrado(tam):
    for count in range(4):
        turtle.forward(tam)
        turtle.left(90)
        
    
    
deseha_quadrado(tamanho_lado)