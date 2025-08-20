def preco(p):
# calcula o valor a pagar em centavos para um peso 'p' em quilos.
    # o valor é R$ 12,00 por quilo, que é 1200 centavos
    return int(round(p * 1200))

# pede o peso do prato ao usuário
peso = float(input('digite o peso do prato em quilos (ex: 0.750): '))

# usa a função para calcular o valor em centavos
valorCentavos = preco(peso)

# imprime o valor formatado para o usuário
print('o valor a pagar é: R$ {:.2f}'.format(valorCentavos / 100))