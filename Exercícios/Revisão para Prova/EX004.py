# números palíndromos são aqueles que tem o mesmo valor se lidos da esquerda para direita ou da direita para esquerda. 
# por exemplo, 44, 232, 123321. 
# faça um programa que imprima todos os números entre 0 e 10.000 que são palíndromos.

def ehPalindromo(numero):
    valor = str(numero)
    return valor == valor[::-1]

def imprimePalindromo():
    for numero in range(0, 10001):
        if ehPalindromo(numero):
            print(numero)

imprimePalindromo()