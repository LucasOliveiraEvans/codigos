#sets - conjuntos em python (tipo set).
#sets em python são mutaveis,porem aceiteam apenas
#tipos imutaveis como valor interno.

#criando um set
#set(iteravel) ou {1,2,3}
#s1 = set('luiz')
#s1 = set() -->vazio
#s1 = {'luiz',1,2,3} ---->com dados

#sets são eficientes para remover valores duplicados
#de iteraveis.
# - eles não tem indexes;
# - eles não garantem ordem;
# - eles são iteraveis (for,in,not in)
#s1 = {1, 2, 3, 3, 3, 3, 3, 1}
#print(s1)


#métodos uteis:
#add, update, clear, discard
#S1 = set()
#s1.add('luiz')
#s1.add(1)
#s1.update(('ola mundo',1,2,3,4))
#s1.clear()
#s1.discard('ola mundo')
#s1.discard('luiz')
#print(s1)

#operadores uteis:
#união: --> | <--  uniao (union) - une
#intersecção: --> & <-- (intersection)  itens presentes em ambos
#diferença: --> - <-- itens presentes apenas no set da esquerda
#diferença simétrica: --> ^ <--   itens que não estão em ambos
#s1 = {1,2,3}
#s2 = {2,3,4}
#s3 = s1 | s2
#s3 = s1 & s2
#s3 = s1 - s2
#s3 = s1 ^ s2
#print(s3)
#
#
#
#
#
#
#
#
#
#
#