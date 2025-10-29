dicionario = {1: 1, 2: 2, 3: 4}

def contarPontos(i, dicionario):
    if i in dicionario:
        return dicionario[i]
    else:
        resposta = contarPontos(i-1, dicionario) + contarPontos(i-2, dicionario) + contarPontos(i-3, dicionario)
    dicionario[i] = resposta
    return resposta

print(contarPontos(100, dicionario))