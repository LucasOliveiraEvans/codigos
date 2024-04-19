#unir as listas usando os valores da menor lista
#['salvador','ubatuba','belo horizonte']
#['BA','SP','MG','RJ']
#resultado --> [('salvador','BA'), ('ubatuba','SP'),('belo horizonte'),'MG']

def zipper (l1,l2):
    intervalo_maximo = min(len(l1), len(l2))
    return [
        (l1[i], l2[i]) for i in range(intervalo_maximo)
    ]
    
l1 = ['salvador', 'ubatuba', 'belo horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))

#outra forma, propria do python é utilizando zip
print(list(zip(l1, l2)))

#caso queira fazer o contrario (usar os valores da lista maior)
#é nescessario usar import
from itertools import zip_longest

print(list(zip_longest(l1, l2, fillvalue='sem cidade')))
#                               ^-- é utilizado para preencher os espaços vazios