def ehPrimo(numero):
    # números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False
    # checa divisores de 2 até a raiz quadrada de número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# lista para armazenar os números primos encontrados
primos = []

# startando a verificação a partir do número 2
num = 2

print('os primeiros 100 números primos são: ')

# loop para encontrar os primeiros 100 números primos
while len(primos) < 100:
    if ehPrimo(num):
        primos.append(num)
    num += 1

print(primos)