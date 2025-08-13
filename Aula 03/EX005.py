from random import randint

numero = randint(1, 10)

while True:
    palpite = int(input('\ntente adivinhar o número (dica: 1 até 10): '))
    if (palpite != numero):
        print('\nvocê errou!')
        if (palpite > numero):
            print('\no número é menor que o seu palpite!')
        else:
            print('\no número é maior que o seu palpite!')
    else: 
        print('\nvocê acertou!')

