'''
argumentos nomeados e não nomeados em funções python
argumentos nomeados tem nome com sinal de igual
argumentos não nomeados recebe apenas o argumento (valor)
'''

def soma(x, y, z):
    #definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ',x + y + z)
    
soma(1,2,3)
soma(1, 2, 3)
soma(1, y=2) #5) #se apenas 1 argumento for nomeado, todos os outros devem ser também

print(1, 2, 3, sep='-')