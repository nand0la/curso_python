lista_tarefa = []

def insert_tarefa():
    print()
    tarefa = input('Digite sua tarefa: ')
    lista_tarefa.append(tarefa)

def listar_tarefa():
    for i in lista_tarefa:
        print(i)

def refazer_tarefa():
    lista_tarefa.pop()
    input_tarefa_refeita = input('Reescreva a tarefa: ')
    lista_tarefa.append(input_tarefa_refeita)

def apagar_tarefa():
    lista_tarefa.pop()
    
# logica

while True:
    print()
    input_tarefa = input('Deseja inserir uma terefa? [s] [n] ')
    if input_tarefa.lower() == 's':
        insert_tarefa()
        listar_tarefa()

    
    if len(lista_tarefa) != 0:
        print()
        input_refazer = input('Deseja refazer a ultima tarefa? [s] [n] ')

        if input_refazer.lower() == 's':
            refazer_tarefa()
            listar_tarefa()

        print()
        input_excluir = input('Deseja excluir a ultima tarefa? [s] [n] ')

        if input_excluir.lower() == 's':
            apagar_tarefa()
            listar_tarefa()

