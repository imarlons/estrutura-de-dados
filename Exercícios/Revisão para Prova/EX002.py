# implemente uma classe para representar uma pilha. 
# você pode usar qualquer representação interna que desejar. 
# a classe deve possuir somente dois métodos: 
# empilha (que adiciona um novo elemento na pilha)
# e 
# desempilha (que remove um elemento da pilha e o retorna). 
# o elemento a ser removido  ́e sempre o elemento mais recentemente empilhado.

class Pilha:
    def __init__(self):
        self.itens = []

    def empilha(self, elemento):
        self.itens.append(elemento)

    def desempilha(self):
        if len(self.itens) == 0:
            return None
        return self.itens.pop() # remove o elemento mais recente da lista/topo da pilha

pilha = Pilha()

pilha.empilha(5)
pilha.empilha(10)
pilha.empilha(15)

print(pilha.desempilha()) # 15
print(pilha.desempilha()) # 10

pilha.empilha(20)

print(pilha.desempilha()) # 20