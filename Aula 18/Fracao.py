class Fracao(object):
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        if self.denominador == 1:
            return str(self.numerador)
        else:
             return str(self.numerador) + '/' + str(self.denominador)
    
    def __add__(self, outraFracao):
        # deve retornar uma fração
        parteCima = self.numerador * outraFracao.denominador + outraFracao.numerador * self.denominador
        parteBaixo = self.denominador * outraFracao.denominador
        return Fracao(parteCima, parteBaixo)

    def __mul__(self, outraFracao):
        # deve retornar uma fração
        parteCima = self.numerador * outraFracao.numerador
        parteBaixo = self.denominador * outraFracao.denominador
        return Fracao(parteCima, parteBaixo)
        
    def obterInverso(self):
        # retorna o inverso da fração atual
        return Fracao(self.denominador, self.numerador)

    def inverte(self):
        # transforma a fração atual para que ela fique com o valor inverso.
        self.numerador, self.denominador = self.denominador, self.numerador

# fracaoA = Fracao(3, 4)
# print(fracaoA.obterInverso())
# fracaoA.inverte()
# print(fracaoA.numerador, fracaoA.denominador)

# fracaoB = Fracao(2, 3)
# mult = fracaoA * fracaoB
# print(mult)

fracaoC = Fracao(3, 1)
# print(fracaoC)

fracaoD = Fracao(2, 2)
add = fracaoC + fracaoD
print(add)