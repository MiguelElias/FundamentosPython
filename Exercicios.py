# coding=utf-8
# exercicio 1
def calcula_consumo (consumo,pessoas,taxa):
    consumo = consumo + taxa
    total = consumo
    total = str(total)
    total = total.replace('.', ',')
    print('O valor total da conta, com a taxa de servico, sera de R$ {}.'.format(total) )
    consumo = consumo/pessoas
    consumo = str(consumo)
    consumo = consumo.replace('.', ',')
    print('Dividindo a conta por {} pessoa(s), cada pessoa devera pagar R$ {} '.format(pessoas,consumo))

consumo = float (input('Informe o valor total do consumo: R$ '))
pessoas = int(input('Informe o total de pessoas: '))
taxa = float(input('Informe a taxa de trabalho entre 0 a 100 : '))

if (pessoas <= 0) or (taxa < 0) or (taxa > 100):
    print('Valor invalido')
if (pessoas > 0) and ((taxa > 0) or (taxa < 100)):
    calcula_consumo(consumo, pessoas, taxa)
#exercicio 2
def verifica_eleitor(idade):
    if idade < 16:
        print('Nao tem direito a voto.')

    elif idade > 16 or idade < 70:
        if idade < 18 or idade > 70 :
            print('Nao tem obrigacao de votar')
        elif idade == idade :
            print('Tem obrigacao de votar.')



idade = int(input('Informe a idade: '))
verifica_eleitor(idade)
#exercicios3
lista_nomes = []
lista_notas = []
participantes =int(input('Digite o numero de participantes: '))
i  = 0
while i < participantes :
  print('Digite o nome do {i+1}º  participante ')
  nome =input()
  print('Digite a nota do  {i+1}º participante ')
  nota = float(input())
  lista_nomes.append(nome)
  lista_notas.append(nota)
  i=i+1


x = 0
armazena_maior = 0
while x < len(lista_notas):
  if lista_notas[x] > armazena_maior:
    armazena_maior = x
  x=x+1

print(x)














