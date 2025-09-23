# Trabalho 1
# Nome do Estudante:
estudante = 'Marlon da Silva'

import random
import string

# -----------------------------------
# CÓDIGO AUXILIAR
# -----------------------------------

ARQUIVO_LISTA_PALAVRAS = "palavras.txt"

def carregar_palavras():
    """
    SAÍDA: lista, uma lista de palavras válidas.  As palavras
    são strings em letra minúscula.

    Dependendo do tamanho da lista de palavras, esta função pode
    demorar um pouco para terminar.
    """
    print("Carregando lista de palavras de arquivo...")
    # noArquivo: arquivo
    noArquivo = open(ARQUIVO_LISTA_PALAVRAS, 'r')
    # linha: string
    linha = noArquivo.readline()
    # lista_de_palavras: list of strings  
    lista_de_palavras = linha.split()
    print(" ", len(lista_de_palavras), "palavras carregadas.")
    return lista_de_palavras

def escolhe_palavra(lista_de_palavras):
    """
    ENTRADA: 'lista_de_palavras': uma lista de palavras (strings)
    SAÍDA: Uma palavra escolhida da lista
    """
    return random.choice(lista_de_palavras)

# -----------------------------------
# FIM DO CÓDIGO AUXILIAR
# -----------------------------------

# Carrega a lista de palavras para ser acessível de qualquer parte do programa
lista_de_palavras = carregar_palavras()

def jogador_venceu(palavra_secreta, letras_escolhidas):
    """
    ENTRADA: 'palavra_secreta', uma string em letras minúsculas que o usuário
             deve adivinhar
             'letras_escolhidas': lista de letras minúsculas que o jogador
             escolheu até agora para adivinhar a palavra
    SAÍDA: True, se todas as letras de 'palavra_secreta' estão em 
           'letras_escolhidas' e False caso contrário
    """
    # ESCREVA SEU CÓDIGO AQUI E APAGUE "pass":
    pass


def progresso_atual_da_palavra(palavra_secreta, letras_escolhidas):
    """
    ENTRADA: 'palavra_secreta', string em letra minúscula que usuário está
             adivinhando.
             'letras_escolhidas', uma lista de letras minúsculas que o jogador
             escolheu até agora
    SAÍDA: Uma string formada por letras e asteriscos (*) que representam letras
           na palavra secreta que ainda não foram adivinhadas
    """
    # ESCREVA SEU CÓDIGO AQUI E APAGUE "pass":
    pass


def letras_ainda_disponiveis(letras_escolhidas):
    """
    ENTRADA: 'letras_escolhidas', lista de letras minúsculas que o usuário
             escolheu até agora.
    SAÍDA: Uma string formada por todas as letras que ainda não foram escolhidas.
           As letras devem ser retornadas em ordem alfabética.
    """
    # ESCREVA SEU CÓDIGO AQUI E APAGUE "pass":
    pass



def forca(palavra_secreta, com_ajuda):
    """
    ENTRADA: 'palavra_secreta', uma string representando uma palavra a ser
             adivinhada
             'com_ajuda', um valor booleano que ativa a funcionalidade de ajuda
             se verdadeiro

    Isso inicia um jogo interativo de Forca.

    * No começo do jogo, deixe o usuário saber quantas letras
      a string 'palavra_secreta' contém e quantas tentativas ele tem de
      escolher letras.

    * O usuário deve começar com 10 tentativas.

    * Antes de cada rodada, você deve mostrar ao usuário quantas tentativas
      ele ainda tem  e as letras que ele ainda não escolheu.

    * Peça ao usuário para escolher uma letra por rodada. Lembre-se de
      checar se o usuário realmente está inserindo uma só letra (ou
      o caractere de ajuda  '!' se a funcionalidade de ajuda está ativa)

    * Se o usuário escolher uma consoante incorreta, ele perde UMA tentativa,
      mas se ele escolher uma vogal incorreta (a, e, i, o, u),
      então ele perde DUAS tentativas.

    * O usuário deve receber informações imediatamente
      após cada tentativa de escolher uma letra para que ele saiba
      se a letra escolhida aparece na palavra secreta.

    * Depois de cada escolha, você deve mostrar ao usuário a palavra
      parcialmente adivinhada até agora.

    -----------------------------------
    A funcionalidade 'com_ajuda' 
    -----------------------------------
    * Se a escolha for o símbolo !, você deve revelar ao usuário uma das letras
      faltantes da palavra ao custo de 3 tentativas. Se o usuário não tem
      3 tentativas restantes, imprima uma mensagem de aviso. Do contrário,
      adicione esta letra à lista de letras adivinhadas e continue jogando
      normalmente.
    """
    # ESCREVA SEU CÓDIGO AQUI E APAGUE "pass":
    pass



# Quando você terminar a função 'forca', vá até o fim do arquivo descomentando
# as linhas indicadas para poder testar seu jogo

if __name__ == "__main__":
    # Para testar seu jogo, descomente as seguintes 3 linhas:

    # palavra_secreta = escolhe_palavra(lista_de_palavras)
    # com_ajuda = False
    # forca(palavra_secreta, com_ajuda)

    # Depois que você implementar a funcionalidade 'com_ajuda', mude
    # o valor de 'com_ajuda' acima para e tente testar usando "!" como
    # letra escolhida!

    ###############
    pass

