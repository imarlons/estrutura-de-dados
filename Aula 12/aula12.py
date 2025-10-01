# Exceções e Asserções

# numeros = [1, 2, 3]
# IndexError: list index out of range
# print(numeros[4])

# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'type'
# inteiro = int(list)

# NameError: name 'vogais' is not defined
# print(vogais)

# TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print('4' / 2)

def somaDosDigitos(string):
    # string = string só com dígitos númericos

    total = 0

    for digito in string:
        try:
            total += int(digito)
        except:
            print('não da pra converter: {}'.format(digito))
    return total

# print(somaDosDigitos('123'))
# print(somaDosDigitos('123abc'))
    
try:
    valorA = int(input('informe um número: '))
    valorB = int(input('informe outro número: '))
    print(valorA / valorB)
except ZeroDivisionError:
    print('ERRO! divisão por zero!')
except ValueError:
    print('ERRO! você precisa informar um número!')
except:
    print('ERRO! algo deu errado!')