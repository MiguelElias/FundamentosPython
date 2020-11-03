class Conta:
    def __init__(self,numero,agencia,saldo,nome):
        self.numero = numero
        self.agencia = agencia
        self.saldo= saldo
        self.nome = nome
    def set_numero(num):
        numero = num
    def get_numero(self):
        return self.numero
    def depositar(self,valor):
        if(valor < 0):
            print('Valor invalido')
        else:
            self.saldo = self.saldo+valor
    def sacar(self,valor):
        self.saldo = self.saldo - valor

c1 = Conta(10,272,50.00,"Miguel")
print(c1.nome)
