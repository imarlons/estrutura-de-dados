# implemente uma classe para representar uma fila. você pode usar qualquer representação interna que desejar. 
# a classe deve possuir somente dois métodos: 
# enfileira (que adiciona um novo elemento na fila) 
# e
# desenfileira (que remove um elemento da fila e o retorna). 
# o elemento a ser removido  ́e sempre o elemento mais antigo que foi enfileirado.

class Fila:
    def __init__(self):
        self.itens = []

    def enfileira(self, elemento):
        self.itens.append(elemento)

    def desenfileira(self):
        if len(self.itens) == 0:
            return None
        return self.itens.pop(0) # remove o elemento mais antigo da lista/fila

fila = Fila()

fila.enfileira(5)
fila.enfileira(10)
fila.enfileira(15)

print(fila.desenfileira()) # 5
print(fila.desenfileira()) # 10