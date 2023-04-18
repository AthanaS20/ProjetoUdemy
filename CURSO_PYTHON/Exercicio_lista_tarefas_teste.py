lista = []
lista_tarefas_desfeitas = []


def listar_tarefas():
    print('\n TAREFAS', *lista, sep='\n')

def acumulador_tarefas(tarefas):
    lista.append(tarefas)
    

def principal():
    while True:
        comando_usuario = input('Digite uma tarefa ou comando: ')
        if comando_usuario == 'listar':
            listar_tarefas()
        if comando_usuario == 'refazer':
            task = lista_tarefas_desfeitas.pop()
            lista.append(task)
            listar_tarefas() #Não está reconhecendo comando refazer    
        if comando_usuario == 'desfazer':
            tarefas_desfeitas = lista.pop()
            lista_tarefas_desfeitas.append(tarefas_desfeitas)
            listar_tarefas()
        else:
            acumulador_tarefas(comando_usuario)
            listar_tarefas()

principal()