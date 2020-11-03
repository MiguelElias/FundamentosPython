#Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
tupla = ('Miguel','Elias','Dias','Manoel','Joaquin','Cassio')
def FatiaTupla(tupla):
    tupla1=()
    tupla2=()
    tamanho = len(tupla)
    metade = int(tamanho/2)
    for x in range (0,metade):
        tupla1 += (tupla[x],)
    for x in range (metade,tamanho):
        tupla2 += (tupla[x],)
    print(f'Primeira metade {tupla1}')
    print(f'Primeira metade {tupla2}')

FatiaTupla(tupla)