#Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive.
#O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.

def Calcula(numero_final):
    somatoria = 0
    for x in range (1,numero_final):
        if x%2 != 0:
            somatoria = somatoria +x            
    return somatoria 


numero = 0
while numero <= 0:
    numero = int(input('Digite um número maior que 0:'))

print (f'A somatoria total é: {Calcula(numero)}')
