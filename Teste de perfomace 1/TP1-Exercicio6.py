#6. (Desafío) Utilizando a ferramenta turtle,
#desenhe os ângulos de um círculo como indicado na figura a seguir:
import turtle 
turtle.title("Questão 6 TP1")
turtle.shape("circle")

def circulo():
    for x in range(0,360,15):
        turtle.setheading(x)
        turtle.forward(100)
        turtle.write(f'{x}°')
        turtle.backward(100)
        
        
turtle.listen()
circulo()
