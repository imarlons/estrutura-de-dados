# escreva uma função que receba uma string com uma expressão matemática que contém 
# parênteses, chaves e colchetes. 
# # por exemplo: "(1+3)*4-2(1+x)". 
# a função deve retornar verdadeiro se parênteses, chaves e colchetes os  estiverem balanceados. 
# isto é, se todo parêntese, chave e colchete que for aberto, for corretamente fechado; 
# e também se não houver o fechamento de um parêntese, chave e colchete que nunca foi aberto.
# exemplo:
# balanceado("(a + b) * (c - (d))") # True
# balanceado("(a + b]") # False

def balanceado(expressao):
    pilha = []

    paresValidos = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for caracter in expressao:
        # se abrir, empilha
        if caracter in '([{':
            pilha.append(caracter)
        # se fechar, tenta combinar
        elif caracter in ')]}':
            if not pilha: # tenta fechar sem ter aberto
                return False
            if pilha[-1] != paresValidos[caracter]: # tipo errado de fechamento
                return False
            pilha.pop() # combina corretamente

            
    return len(pilha) == 0

print(balanceado("(a + b) * [c - {d}]"))      # True
print(balanceado("([{}])"))                   # True
print(balanceado("([)]"))                     # False
print(balanceado("(a + b]"))                  # False
print(balanceado("{[()]}"))                   # True
print(balanceado("{[()]}]"))                  # False

