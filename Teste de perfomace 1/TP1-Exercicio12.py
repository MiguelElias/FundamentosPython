#12. Faça uma função no Python que, utilizando a ferramenta turtle,
#desenhe um círculo de raio N.
import  turtle

raio = 0
while (raio==0 ):
    raio = int(input('Tamanho do raio: '))

def circulo(raio):
    turtle.circle(raio)
        
circulo(raio)