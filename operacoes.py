def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    return media < 6

def exibir_reprovados(dados_alunos, matriculas_reprovados):
    for matricula in matriculas_reprovados:
        aluno = dados_alunos[matricula]
        nome = aluno['nome']
        media = aluno['media']
        print(f"Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media}")