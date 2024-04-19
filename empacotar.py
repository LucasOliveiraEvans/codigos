'''
empacotamento: colocar valores em uma lista
desempacotamento: 'tirar' valores de uma lista
a variavel 'nome1' desempacota

'''

nomes = ['maria','alberto','carla']

nome1,*_= nomes
print(nome1,_)

'''
a variavel 'nome1' desempacotou o nome 'maria'
usando * pega o 'resto' dos valores
'''