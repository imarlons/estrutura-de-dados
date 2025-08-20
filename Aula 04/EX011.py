# Faça um algoritmo (encapsulado em uma função)  que leia um salário de um funcionário e o aumente em 15%. Após o aumento, desconte 5% de impostos. Imprima o salário inicial, o salário com o aumento e o salário final.

# Use as seguintes funções:

# def calcula_aumento(v):
#     """ ENTRADA: Um valor numérico 'v' representando um salário.
#          SAÍDA:  O valor inicial 'v' após passar por um aumento de 15% """

# def calcula_desconto(v):
#     """ ENTRADA: Um valor numérico 'v' representando um salário.
#          SAÍDA:  O valor inicial 'v' após passar por um desconto de 8% de impostos"""

# def calcula_salario_final(v):
#     """ ENTRADA: Um valor numérico 'v' representando um salário.
#          SAÍDA:  O valor inicial 'v' após passar por todos os  descontos e aumentos previstos"""

def calcularAumento(salario):
    return salario * 1.15
    
def calcularDesconto(salario):
    return salario * 0.95

def calcularSalarioFinal(salario):
    salarioComAumento = calcularAumento(salario)
    salarioFinal = calcularDesconto(salarioComAumento)
    return salarioFinal

salarioInicial = float(input('informe o seu salário: R$'))
salarioComAumento = calcularAumento(salarioInicial)
salarioFinal = calcularSalarioFinal(salarioInicial)

print('salário base: R${:.2f}'.format(salarioInicial))
print('salário com aumento: R${:.2f}'.format(salarioComAumento))
print('salário com desconto: R${:.2f}'.format(salarioFinal))




