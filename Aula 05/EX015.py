def aplica(criterio, n):
    contador = 0
    for i in range(n + 1):
        if criterio(i):
            contador += 1
    return contador

def par(x):
    return x % 2 == 0

def maiorQue5(x):
    return x > 5

print(aplica(par, 10))
print(aplica(maiorQue5, 4))