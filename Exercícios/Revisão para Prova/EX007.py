# implemente uma função intercala(l1, l2) que recebe duas listas l1 e l2 de mesmo tamanho 
# e retorna uma nova lista contendo os elementos intercalados.
# exemplo: intercala([1,2,3], [’a’,’b’,’c’]) 
# deve produzir [1, ’a’, 2, ’b’, 3, ’c’]

def intercala(listaA, listaB):
    resultado = []
    for i in range(len(listaA)):
        resultado.append(listaA[i])
        resultado.append(listaB[i])
    return resultado

print(intercala([1, 2, 3], ['a', 'b', 'c']))

# def intercala(listaA, listaB):
#     resultado = []
#     for a, b in zip(listaA, listaB):
#         resultado.extend([a, b])
#     return resultado
