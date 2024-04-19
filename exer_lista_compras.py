import os

lista=[]
while True:
    print('selecione uma opção')
    opcao=input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        
        valor=input('digite o nome do produto: ')
        lista.append(valor)

    elif opcao == 'a':
        os.system('cls')
        
        indice_digitado= input('escolha o indice para apagar: ')
        try:
            indice=int(indice_digitado)
            del(lista[indice])
        except IndexError:
            print('indice nao existe na lista')
        except ValueError:
            print('por favor digite numeros inteiros')

    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('nada para listar')

        for i,valor in enumerate(lista):
            print(i,valor)
    else:
        print('por favor digide i, a ou l')
