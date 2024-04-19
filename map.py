#map - criar uma nova lista com o mesmo numero de dados que a antiga

from functools import reduce
from operator import add

def soma_nat(n):
    #return sum([i for i in range(1,n+1)])
    return reduce(add,range(1,n+1))


numero = int(input())
print(f'A soma dos números de 1 a {numero} é {soma_nat(numero)}')