salario = float(input('informe o seu salário mensal: R$'))
percentual_economia = float(input('digite a porcentagem que consegue economizar (%): '))
preco_casa = float(input('digite o preço da casa: R$ '))

# cálculo do valor de entrada (25% do preço da casa)
entrada_casa = preco_casa * 0.25

# conversão da porcentagem para valor mensal
economia_mensal = salario * (percentual_economia / 100)

# juros mensais (0,5%)
taxa_juros = 0.005

# contadores
saldo = 0
meses = 0

while (saldo < entrada_casa):
    saldo += economia_mensal # economia do mês
    saldo += saldo * taxa_juros # rendimento da poupança
    meses += 1

print(f'você precisará de {meses} meses para juntar o valor da entrada.')