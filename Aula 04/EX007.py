def ehPrimo(numero):
    # se o número for menor que 2, não é primo.
    if numero < 2:
        return False
    # checa se o número é divisível por qualquer valor entre 2 e ele mesmo.
    for i in range(2, numero):
        if numero % i == 0:
            return False
    # se não encontrou nenhum divisor, é primo.
    return True

primosEncontrados = 0
start = 2

print('os primeiros 100 números primos são: ')
while primosEncontrados < 100:
    if ehPrimo(start):
        print(start, end='\n')
        primosEncontrados += 1
    start += 1

print('\n')