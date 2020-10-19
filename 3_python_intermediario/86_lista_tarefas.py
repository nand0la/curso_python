lista_tarefa = []

def add_tarefa(tarefa):
    lista_tarefa.append(tarefa)


def remover_tarefa():
    lista_tarefa.pop()


def listar_tarefa():
    print(lista_tarefa)


def refazer_tarefa(nova_tarefa):
    lista_tarefa.pop()
    lista_tarefa.append(nova_tarefa)


while True:
    print()
    input_add_tarefa = input('Deseja adicionar tarefa? [s] [n] ')
    
    if input_add_tarefa.lower() == 's':
        print()
        input_nova_tarefa = input('Digite sua tarefa: ')
        add_tarefa(input_nova_tarefa)
        listar_tarefa()


    if len(lista_tarefa) > 0:
        print()
        input_remover_tarefa = input('Deseja remover tarefa? [s] [n] ')

        if input_remover_tarefa.lower() == 's':
            remover_tarefa()
            listar_tarefa()

        
        print()
        input_refazer_tarefa = input('Deseja refazer tarefa? [s] [n] ')
        
        if input_refazer_tarefa.lower() == 's':
            print()
            input_tarefa_refeita = input('Reescreva a tarefa: ')
            refazer_tarefa(input_tarefa_refeita)
            listar_tarefa()


