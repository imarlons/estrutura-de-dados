def divisao_pareada(Lnum, Ldem):
    """
    ENTRADA: Lnum e Ldem são duas listas de mesmo tamanho contendo dígitos
    SAÍDA: Uma nova lista contendo o resultado da divisão de cada item 
    de Lnum pelo item correspondente em Ldem que está na mesma
    posição.
    """
    
    # verifica se as listas têm o mesmo tamanho, embora o enunciado garanta
    if len(Lnum) != len(Ldem):
        raise ValueError("as listas de entrada devem ter o mesmo tamanho.")
        
    resultado = []
    
    # percorre as listas usando a função zip para iterar sobre os pares (numerador, denominador)
    for num, dem in zip(Lnum, Ldem):
        # verifica a condição de divisão por zero
        if dem == 0:
            # levanta a exceção ValueError, conforme o exemplo
            raise ValueError("tentativa de divisão por zero na lista de denominadores (Ldem).")
        
        # realiza a divisão e adiciona o resultado à lista
        resultado.append(num / dem)
        
    return resultado

L1 = [10, 20, 30, 40, 50]
L2 = [5, 4, 3, 2, 1]

print(divisao_pareada(L1, L2))