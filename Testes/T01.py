from random import randint

numeros = [randint(1, 10) for i in range(10)]
numerosFormatados = set(numeros) # lista com os valores únicos de "numeros"

impar, par = [], []

for valor in numerosFormatados:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print('''
    lista original: {}
    lista formatada: {}
    lista ímpar: {}
    lista par: {}
'''.format(numeros, numerosFormatados, impar, par))