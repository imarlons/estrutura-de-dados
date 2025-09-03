# escreva uma função que satisfaz a seguinte especificação:

def conta_numeros_com_raiz_perto_de(n, epsilon):
    """
    ENTRADA: 'n' é um inteiro maior que 2
                       'epsilon' é um inteiro positivo  menor que 1
    SAÍDA: Retorna quantos números inteiros tem uma raíz quadrada próxima de 'n'.
                 Uma raíz quadrada próxima é aquela que tem uma distância menor que 'epsilon' do valor 'n'.
    """
    contador = 0
    # O loop deve começar a partir de n*n, que é onde a raiz é igual a n.
    # Vamos considerar um intervalo seguro para encontrar os números.
    # (n - epsilon)**2 e (n + epsilon)**2 delimitam o intervalo
    # dos números cuja raiz quadrada está entre n-epsilon e n+epsilon.

    # O loop precisa percorrer os números inteiros.
    # Em Python, o loop 'for' é o mais adequado para iterar sobre um intervalo.
    # O intervalo de busca pode ser estimado:
    # A raiz de (n - epsilon)**2 é n - epsilon
    # A raiz de (n + epsilon)**2 é n + epsilon
    # Logo, os números que procuramos estão entre (n-epsilon)**2 e (n+epsilon)**2.
    # O +2 no final garante que o loop inclua o limite superior, pois o range em Python
    # não inclui o último valor.

    limite_inferior = int((n - epsilon)**2)
    limite_superior = int((n + epsilon)**2) + 2 

    for numero in range(limite_inferior, limite_superior):
        # A raiz quadrada de um número é o número elevado a 0.5
        raiz_quadrada = numero ** 0.5
        
        # A distância entre a raiz quadrada e n é o valor absoluto da diferença.
        distancia = abs(raiz_quadrada - n)
        
        # Verifica se a distância é menor que epsilon
        if distancia < epsilon:
            contador += 1
            
    return contador

# DICA: Calcular a raíz quadrada é a mesma coisa que elevar à (1/2), ou 0.5.
# EXEMPLO: print(conta_numeros_com_raiz_perto_de(10, 0.1)) deve imprimir 4, pois os seguintes números tem raíz quadrada próxima:
#     * 99 (a raíz é 9.9498743710662)
#     * 100 (a raíz é 10)
#     * 101 (a raíz é 10.04987562112089)
#     * 102 (a raíz é 10.099504938362077)

print(conta_numeros_com_raiz_perto_de(10, 0.1)) # Deve imprimir 4
print(conta_numeros_com_raiz_perto_de(3, 0.5))  # Exemplo adicional: Deve retornar 5 (8, 9, 10, 11, 12)

# PRECISO ESTUDAR ESSA SOLUÇÃO COM MAIS PRECISÃO, PARA ENTENDER O QUE OCORRE DE FATO