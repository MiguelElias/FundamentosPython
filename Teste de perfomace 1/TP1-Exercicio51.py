#5. Trabalhar com tuplas é muito importante! Crie 4 funções nas quais:

#Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo
tupla = ('Miguel','Elias','Dias','Manoel','Joaquin','Cassio')
p     = input('Digite um nome para pesquisa: ')

def Tuplas(tupla,pesquisa):
    resultado = False
    for i in range(0, len(tupla)):
        if (p.upper() == tupla[i].upper() ):
            resultado = True
    return resultado

if (Tuplas(tupla,p)):
    print(f'O nome {p} existe na tupla ')
else:
    print(f'O nome {p} não existe na tupla ')
    

    
        
