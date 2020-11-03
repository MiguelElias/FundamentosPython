#18. (desafio) Em jogos antigos era possível ver que os desenhos eram compostos por vários triângulos.
#Como uma maneira de treinar isso, a partir do N dado pelo usuário desenhe um polígono de lado N
#composto somente por triângulos como na figura:

import math
import turtle
a = 0 
while(a<=0):
    a = int(input('Digite quantos triângulos terá a primeira figura:  '))
b = 0 
while(b<=0):
    b = int(input('Digite quantos triângulos terá a segunda figura:  '))
c = 0 
while(c<=0):
    c = int(input('Digite quantos triângulos terá a terceira figura:  '))

def draw_pie(t, n, r):
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()


def polypie(t, n, r):
    angulo = 360.0 / n
    for i in range(n):
        isosceles(t, r, angulo/2)
        t.lt(angulo)


def isosceles(t, r, angulo):
    y = r * math.sin(angulo * math.pi / 180)
    t.rt(angulo)
    t.fd(r)
    t.lt(90+angulo)
    t.fd(2*y)
    t.lt(90+angulo)
    t.fd(r)
    t.lt(180-angulo)


tartaruga = turtle.Turtle()

tartaruga.pu()
tartaruga.bk(130)
tartaruga.pd()

tamanho = 40

draw_pie(tartaruga, a, tamanho)
draw_pie(tartaruga, b, tamanho)
draw_pie(tartaruga, c, tamanho)
tartaruga.hideturtle()
turtle.mainloop()
