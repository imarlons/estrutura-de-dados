def contarPontos(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else: 
        return contarPontos(x-1) + contarPontos(x-2) + contarPontos(x-3)
    
print(contarPontos(3))