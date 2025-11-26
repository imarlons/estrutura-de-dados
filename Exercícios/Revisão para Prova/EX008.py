# você receberá uma lista de tuplas (nome, nota) representando alunos e suas notas. 
# exemplo: [("Ana", 8.5), ("João", 7.2), ("Ana", 9.1)]
# crie uma função media_por_aluno(lista) que retorne um dicionário, onde:
# • cada chave é um nome de aluno
# • o valor é a média das notas daquele aluno
# por exemplo, a saída esperada para o exemplo é: {"Ana": 8.8, "João": 7.2}

def mediaPorAluno(lista):
    somaNotas, contagem = {}, {}

    for nome, nota in lista:
        if nome not in somaNotas:
            somaNotas[nome] = 0
            contagem[nome] = 0

        somaNotas[nome] += nota
        contagem[nome] += 1

    medias = {}
        
    for nome in somaNotas:
        medias[nome] = somaNotas[nome] / contagem[nome]

    return medias

exemplo = [('Ana', 8.5), ('João', 7.2), ('Ana', 9.1)]
print(mediaPorAluno(exemplo)) 