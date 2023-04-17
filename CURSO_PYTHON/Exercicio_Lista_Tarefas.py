# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

lists = []
undo_lists = []

commands = [
    'listar',
    'desfazer',
    'refazer',
]



def listar():
    print('\n TAREFAS', *lists, sep='\n')

def desfazer():
    if len(lists) == 0:
        print('Não há mais itens na lista')
        return

    undo_task = lists.pop()
    undo_lists.append(undo_task)
    listar()

def refazer():
    if len(undo_lists) == 0:
        print('Não há itens desfeitos.')
        return
        
    task = undo_lists.pop()
    lists.append(task)
    listar()


def append_list(task):
    lists.append(task)
    listar()

def init():
    user_input = input('Digite uma tarefa ou comando: ')

    if user_input in commands:
        if user_input == 'listar':
            listar()
        if user_input == 'desfazer':
            desfazer()
        if user_input == 'refazer':
            refazer()
        if user_input == 'fechar':
            return True
            
    else:
        append_list(user_input)
        return False

while True:
    if init():
        break

        







