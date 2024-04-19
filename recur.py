from random import randint

def procura(l, n):
    if len(l) == 0:
        return False
    if l[0] == n:
        return True
    return procura(l[1:], n)

lista=[]
for i in range (10):
    lista.append(randint(1,50))
print(lista)
busca=int(input('digite um numero para saber se existe:'))

if procura(lista, busca):
    print("Este numero está na lista!!")
else:
    print("Este numero nao está na lista!!")