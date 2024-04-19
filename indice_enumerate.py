'''
enumerate: enumera iteraveis (indices)
[(0, 'maria'), (1, 'carlos'), (2, 'pedro')]->enumerate enumera cada item de uma lista
fazendo assim uma tupla com o indice e o valor
'''

lista_nomes= ['maria','carlos','pedro']

#lista_enumerada= list(enumerate(lista_nomes))
#print(lista_enumerada)

'''
[(0, 'maria'), (1, 'carlos'), (2, 'pedro')]->enumerate enumera cada item de uma lista
fazendo assim uma tupla com o indice e o valor
'''

#for itens in enumerate(lista_nomes):
#    print(itens)
'''
podendo usar o enumerate no for,para uma proxima vez que for nescessario
usa-lo,os valores retornarao
(senao o enumerate seria usado somente em 1 for,pois os valores seriam 'zerados')
'''


for itens in enumerate(lista_nomes):
    a,b = itens
    print(a,b)

#ou
    
for indice,nome in enumerate(lista_nomes):
    print(indice,nome)
'''
como o formato é uma tupla, o indice pode ser transferido para uma variavel (a)
e o item em outra (b)
'''

