#introdução às generator functions em python

def generator(n=0):
    yield 1 #pausa
    print('continuando...')
    yield 2 #pausa
    print('mais uma vez...')
    yield 3
    print('terminando')
    return 'ACABOU'

gen = generator(n=0)
for n in gen:
    print(n)
    
######################################

def generator(n=0, maximum=10):
    while True:
        yield n
        n+= 1
        
        if n>= maximum:
            return


gen = generator(n=0)
for n in gen:
    print(n)