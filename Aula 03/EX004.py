# solicita os valores de entrada
c = float(input('digite o valor de c: '))
g = float(input('digite o chute inicial g: '))

# calcula novoG usando a fórmula dada
novoG = g - (g**3 - c) / (3 * g**2)

# mostra o resultado
print(f"O novo chute mais próximo do zero é: {novoG:.2f}")
