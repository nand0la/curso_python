'''
    fazer funções de maneira rápida
    usado como função de callback
'''

a = lambda x, y: x + y

aluno_turma = [
    ['Fernando', 200],
    ['Luiz', 300],
    ['Ana', 200],
    ['Witoria', 300],
    ['José', 400],
]

aluno_turma.sort(key=lambda lista: lista[1])
print(aluno_turma)