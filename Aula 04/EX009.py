def palindromo(s):
    return s == s[::-1]

# print('"222" é um palíndromo? {}'.format(palindromo('222')))
# print('"2222" é um palíndromo? {}'.format(palindromo('2222')))
# print('"abc" é um palíndromo? {}'.format(palindromo('abc')))

teste = str(input('escreva algo para saber se é um palíndromo: '))

print('"{}" é um palíndromo? {}'.format(teste, palindromo(teste)))