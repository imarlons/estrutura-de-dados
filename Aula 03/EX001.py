# você acabou de se formar e conseguiu um emprego. 
# você quer comprar uma casa. Mas as casas são caras e você precisa economizar o que sobra de seu salário.
# seu objetivo é descobrir quantos meses é preciso economizar para conseguir pagar o preço de entrada da casa.
# seu programa deve perguntar ao usuário as seguintes informações e armazenar elas como floats:
# a) seu salário mensal
# b) a porcentagem do salário que você consegue economizar. (Exemplo: 12,5%)
# c) o preço da casa
# assuma que você consegue comprar a casa pagando um valor de entrada de 25% do preço da casa,
# e que no começo da cada mês, o valor que você economizou aumenta em 0,5% (pois está em uma caderneta de poupança).
# após receber os valores de entrada, o programa deve gerar uma resposta em meses.

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
