def mantemConsoantes(palavra): 
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    palavraFormatada = ''
    for caractere in palavra:
        if caractere in consoantes:
            palavraFormatada += caractere
    return palavraFormatada


teste = str(input('digite uma palavra: ')).lower()

print('{} sem as vogais fica: {}'.format(teste, mantemConsoantes(teste)))