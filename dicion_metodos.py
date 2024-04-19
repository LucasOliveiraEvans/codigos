#métodos uteis dos dicionarios em python
#len - retorna quantas chaves existem
#keys - iteravel com chaves (nome das chaves)
#values - iteraveis com valores
#items - iteravel com chaves e valores
#setdefault - adiciona valor se a chave nao existe
#copy - retorna uma copia rasa (shallow copy)
#get - obtem uma chave
#pop - apaga um item com a chave especificada (del)
#popitem - apaga o ultimo item adicionado
#update - atualiza um dicionario com outro
#
#
#pessoa={
#   'nome':'luiz otavio',
#  'sobrenome':'miranda',
#}
#
#
#print(len(pessoa))
#print(pessoa.keys())
#
#mas se eu quizer uma chave especifica:
#
#print(list(pessoa.keys())) #ou tuple
#
#print(list(pessoa.values)) #para pegar os valores
#
#print(list(pessoa.items())) #mostra as chaves e valores
#
#
#for chave,valor in pessoa.items:
#   print(chave,valor)
#
#pessoa.setdefault('idade', 33) criei a chave idade e o seu valor é 33
#
##############################################################################
#d1 = {
#   'c1':1,
#   'c2':2,
#   'l1': [0,1,2],
#}
#d2 = d1.copy() assim o d2 faz uma copia de d1
#               senão os 2 apontariam para o mesmo endereço
#
#d2['c1'] = 1000
#print(d1)
#print(d2)
#
#
#               POREM!!!
#nao fará uma copia de valores mutaveis (como a lista)
#para copiar valores imutaveis precisa de uma
#copia profunda (deepcopy)
#
#import copy
#
#d1 = {
#   'c1':1,
#   'c2':2,
#   'l1': [0,1,2],
#}
#d2 = copy.deepcopy(d1)
#
#d2['c1'] = 1000
#d2['l1'][1] = 9999
#
#print(d1)
#print(d2)
#
###################################################################
#
#p1 = {
#   'nome':'luiz',
#   'sobrenome':'miranda',
#}
#print(p1.get('nome'))
#
#           POP
#
#nome = p1.pop('nome')
#print(nome)
#print(p1)
#
#-->caso use pop.item a ultima chave é eliminado
#
##################################################################
#
#usando update---->ele atualiza uma chave
#que ja foi criada OU caso não exista
#ela é criada
#podemos fazer assim:
#
#p1.update({
#       'nome':'novo valor',
#       'idade':30,
#})
#print(p1)
#
#           OU ASSIM
#
#p1.update(nome='novo valor',idade=30)
#print(p1)
#
#
#