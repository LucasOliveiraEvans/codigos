"""
tupla : valor imutavel (não se pode alterar uma)
nao se usa [] para criar uma
pode se converter uma lista em tupla usando 'tuple',o inverso pode acontecer
"""

nomes= ['maria','carlos','pedro']
tupla_nomes= tuple(nomes)
print(tupla_nomes)

'''inverso'''

nomes= 'maria','carlos','pedro'

nomes_lista= list(nomes)
print(nomes_lista)