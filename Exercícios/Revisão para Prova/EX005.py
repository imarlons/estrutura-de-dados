# faça uma função que receba uma string formada por 8 dígitos, um traço  e um último dígito verificador,
# e retorne se ela representa um valor válido (isto é, se seu dígito verificador foi corretamente calculado). 

# o dígito verificador é calculado seguindo o esquema abaixo: 

# cada dígito passa por um multiplicador. em seguida, ao invés de somar  os resultados de cada multiplicação,
#  somamos os dígitos do resultado da  multiplicação (por exemplo: se a multiplicação der 12, somamos os dígitos  1 e 2, obtendo 3). 
# o resultado da soma dos dígitos é então dividido por 10 e obtemos o resto da divisão. 
# se o resto da divisão for zero, este será  nosso dígito verificador. 
# caso contrário, o dígito verificador deve ser 10 menos este resto da divisão.

# XXXXXXXX-X 

def somaDigitos(numero):
    return sum(int(digito) for digito in str(numero))

def calculaDV(valores):
    multiplicadores = [1, 2] * 4 # 8 posições: 1, 2, 1, 2, 1, 2, 1, 2

    somaTotal = 0
    for digito, mult in zip(valores, multiplicadores):
        resultado = int(digito) * mult
        somaTotal += somaDigitos(resultado)

    resto = somaTotal % 10

    if resto == 0:
        return 0
    return 10 - resto

def verificaCodigo(codigo):
    # exemplo de formato: 12345678-9
    parteNumeros, informadoDV = codigo.split('-')
    informadoDV = int(informadoDV)

    calculadoDV = calculaDV(parteNumeros)

    return calculadoDV == informadoDV

print(verificaCodigo('26151314-7')) # True
