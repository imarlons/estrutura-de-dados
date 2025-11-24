# implemente uma função que recebe uma lista de números e imprima o resultado da soma de todos os números 
# dividido pelo resultado da multiplicação de todos os números.

def calculaResultado(lista):
    soma = 0
    multiplicacao = 1

    for numero in lista:
        soma += numero
        multiplicacao *= numero

    if multiplicacao == 0: # para evitar divisão por zero
        print('NÃO É POSSÍVEL DIVIDIR POR ZERO.')
        return
    
    resultado = soma / multiplicacao
    print(resultado)

calculaResultado([1, 2, 3, 4, 5])
calculaResultado([1, 3, 5, 7, 9])