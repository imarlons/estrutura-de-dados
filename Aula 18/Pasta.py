class Pasta:
    def __init__(self, nome):
        self.nome = nome
        self.subPastas = []

    def adicionar(self, subpasta):
        self.subPastas.append(subpasta)

    def __str__(self):
        return self.nome

raiz = Pasta('MEU COMPUTADOR')
driveC = Pasta('C')
driveD = Pasta('D')

raiz.adicionar(driveC)
raiz.adicionar(driveD)

print(raiz.subPastas)
    