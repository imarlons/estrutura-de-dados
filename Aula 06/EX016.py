# escreva uma função que atenda à seguinte especificação:

def conta_caracteres(s):
    """
    ENTRADA: uma string 's' com caracteres em letra minúscula
    SAÍDA: uma tupla onde o primeiro elemento é  o número de vogais e o segundo é o número de consoantes.
    """
    
    contVogal = 0
    contConsoante = 0
    tupla = (contVogal, contConsoante)
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    vogais = 'aeiou'
    for caractere in s:
        if caractere in vogais:
            contVogal += 1
        elif caractere in consoantes:
            contConsoante += 1
    tupla = (contVogal, contConsoante)
    return tupla

# alguns exemplos do comportamento esperado:
print(conta_caracteres("abcd")) # Deve imprimir (1, 3)
print(conta_caracteres("zcght")) # Deve imprimir (0, 5)