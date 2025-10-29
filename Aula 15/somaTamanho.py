# numeros = [30, 40, 50]
palavras = ['oi', 'ai', 'casa']

def somarTamanho(lista):
    resultado = ''
    for i in lista:
        resultado += i
    return len(resultado)

# print(somarTamanho(numeros))
print(somarTamanho(palavras)) # deve imprimir 8
print(somarTamanho([''])) # deve imprimir 0



