import sys

#generator expresion, iterables e iterators em python
iterable = ['eu', 'tenho', '__iter__']
iterator = iter(iterable) #tem __iter__ e __next__
lista = [n for n in range(100)]
generator = (n for n in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)
