#Dada uma tupla e um elemento, elimine esse elemento da tupla.
tupla = ('Miguel','Elias','Dias','Manoel','Joaquin','Cassio')


print('Nomes disponiveis: Miguel,Elias,Dias,Manoel,Joaquin,Cassio')
nome = input('Digite o nome que deseja excluir da lista:  ')
nome = nome.upper()

def VerificaRegistro(tupla,nome):
    a=0
    for x in range (0,len(tupla)):
        if (nome == tupla[x].upper()):
            a=1
    if a == 1:
        return True
    else:
        return False


def ElimiaRegistro(tupla,nome):
    novatupla = ()
    for x in range (0,len(tupla)):
        if (nome != tupla[x].upper()):
            novatupla += (tupla[x],)
    tupla = novatupla
    print(f'O nome "{nome.upper()}" foi removido da tupla')
    print(f'Tupla: {tupla}')
        
while (VerificaRegistro(tupla,nome) == False) :
    print('Registro não existe !! ')
    print('Nomes disponiveis: Miguel,Elias,Dias,Manoel,Joaquin,Cassio')
    nome = input('Digite o nome que deseja excluir da lista:  ')
    nome = nome.upper()
ElimiaRegistro(tupla,nome)



    
    

