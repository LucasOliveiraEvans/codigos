'''
numeros de ponto flutuante (float) podem apresentar imprecisão
'''

numero1= 0.1
numero2= 0.7

numero3= numero1 + numero2

print(numero3) 
''' --> resultado: 0.799999...'''

'''como contornar isso:
podemos formatar o numero
usar o 'round' para arredondar (com o 2° argumento sendo o n° de casas) '''

print(f'{numero3:.2f}')

print(round(numero3, 2))