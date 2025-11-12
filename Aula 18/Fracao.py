class Fracao(object):
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return str(self.numerador) + '/' + str(self.denominador)
        
    def obterInverso(self):
        # retorna o inverso da fração atual
        return Fracao(self.denominador, self.numerador)

    def inverte(self):
        # transforma a fração atual para que ela fique com o valor inverso.
        self.numerador, self.denominador = self.denominador, self.numerador

fracaoA = Fracao(3, 4)
print(fracaoA.obterInverso())
fracaoA.inverte()
print(fracaoA.numerador, fracaoA.denominador)