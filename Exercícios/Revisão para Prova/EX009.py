# escreva uma função que receba uma string com uma expressão matemática que contém parênteses. # por exemplo: "(1+3)*4-2(1+x)". 
# a função deve retornar verdadeiro se os parênteses estiverem balanceados. 
# isto é, se todo parêntese que for aberto, for corretamente fechado; 
# e também se não houver o fechamento de um parêntese que nunca foi aberto.
# exemplo:
# balanceado("(a + b) * (c - (d))") # True
# balanceado("(a + b]") # False

def balanceado(expressao):
    pilha = []

    for caracter in expressao:
        if caracter == '(':
            pilha.append(caracter)
        elif caracter == ')':
            if not pilha:
                return False
            pilha.pop()

    return len(pilha) == 0

print(balanceado("(a + b) * (c - (d))"))  # True
print(balanceado("(a + b]"))              # False
print(balanceado("(1+3)*4-2(1+x)"))       # True
print(balanceado(")("))                   # False
print(balanceado("(()"))                  # False
