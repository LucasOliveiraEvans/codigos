import os

def listar(tarefas):
    print()
    if not tarefas:
        print('nenhuma tarefa para listar')
        print()
        return
    
    print('tarefas:')
    for tarefa in tarefas:
        print(f'{tarefa}')
    print
    
def desfazer(tarefas,tarefas_desfazer):
    print()
    if not tarefas:
        print('nenhuma tarefa para desfazer')
        print()
        return
    
    tarefa = tarefas.pop()
    print(f'tarefa removida: {tarefa=}')
    tarefas_refazer.append(tarefa)
    print()

    
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('nenhuma tarefa para refazer.')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada')
    tarefas.append(tarefa)
    print()

    
def adicionar(tarefa,tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('voce não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada')
    tarefas.append(tarefa)
    print()
    
    
tarefas = []
tarefas_refazer = []

while True:
    print('comandos: listar, desfazer e refazer')
    tarefa = input('digite uma tarefa ou comando:')
    
    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue