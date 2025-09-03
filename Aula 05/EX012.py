# o que é impresso na tela se o seguinte programa Python, armazenado em um arquivo, é executado?

# COMEÇO DO PROGRAMA:
def add(x, y):
  return x + y

def mult(x, y):
  print(x*y)

add(1, 2) # como não há um "print", o terminal não retorna nenhum valor, mas se o mesmo fizesse, o resultado seria 3

print(add(2, 3)) # aqui, a função é acompanhada de um print, o que faz com que o resultado seja impresso no terminal, sendo assim, o resultado é 5.

mult(3, 4) # não há um return no escopo da função, mas há um print que retorna o resultado da operação dos parâmetros, que neste caso, é 12

print(mult(4, 5)) # retorna 20 e None, o 20 faz referência ao print do que acontece na função e o None é o retorno não declarado da função que é extraído pelo print global

