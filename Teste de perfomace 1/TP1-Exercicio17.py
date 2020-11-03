#17. Escreva uma função que receba uma string e um número inteiro x e rotacione a string x posições
#para a esquerda. Assuma que a string tem pelo menos x caracteres.
#Isto é, utilizando como entradas a string “aeiou” e o inteiro 3, o resultado da sua função deve ser “ouaei”.
string=input('Digite uma string: ')
num = len(string) + 1 
while (num > len(string)):
    num = int(input(f'Digite um numero menor que {len(string)}: '))  
string2 = string[num::]
string2 = string2+string[0:num]
string  = string2
print(string)



