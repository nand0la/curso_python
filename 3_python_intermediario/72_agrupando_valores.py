from itertools import groupby, tee

alunos = [
    {'nome': 'Fernando', 'nota': 100},
    {'nome': 'Andre', 'nota': 200},
    {'nome': 'Julia', 'nota': 100},
    {'nome': 'Ana', 'nota': 300},
    {'nome': 'Leonardo', 'nota': 100},
    {'nome': 'Júlia', 'nota': 100},
]

alunos.sort(key=lambda x: x['nota'])
alunos_agrupados = groupby(alunos, lambda x: x['nota'])
for aluno, turma in alunos_agrupados:
    print(aluno)
    for alunos_turma in turma:
        print(alunos_turma)
