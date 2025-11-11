import random

for A in range(1,6):
    print('\nConjunto {}'.format(A))
    for B in range(5):
        numero = random.randint(1, 100)
        print('Valor: {}'.format(numero))