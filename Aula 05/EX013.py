# o código abaixo tem erros. corrija-o.

# início do código:
def eh_triangular(n):
    """
    entrada: um inteiro positivo 'n'.
    saída: True, se 'n' é um número triangular. Isto é, ele é a soma de números naturais
           sequenciais começando em 1. Exemplo: 1+2+3+...+k
    """
    total = 0
    i = 1
    while total < n:
        total += i
        if (total == n):
            return True
        i += 1
    return False

# testando o código
print(eh_triangular(4)) # deve imprimir 'False'
print(eh_triangular(6)) # deve imprimir 'True'
print(eh_triangular(1)) # deve imprimir 'True'