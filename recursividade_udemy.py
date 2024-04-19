#funções recursivas e recurvidades
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes moneres

def recursiva(inicio=0,fim=4):
    
    print(inicio,fim)
    
    #caso base
    if inicio >= fim:
        return fim
    
    inicio +=1
    return recursiva(inicio,fim)

print(recursiva())