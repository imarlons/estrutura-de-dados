# escreva uma função conta_vogais(s) que recebe uma string ‘s’ 
# e retorna um dicionário indicando quantas vezes cada vogal (a, e, i, o, u) aparece na string. 
# a contagem deve ignorar a diferença entre maiúsculas e minúsculas.
# vogais que não aparecem devem ter o valor 0 no dicionário.

def contaVogais(string):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} 
    
    string = string.lower()

    for caracter in string:
        if caracter in vogais:
            vogais[caracter] += 1
    
    return vogais

print(contaVogais('abacate'))
