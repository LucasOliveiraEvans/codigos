'''def multiplos(*args):
    resultado= 1
    for numeros in args:
        resultado *= numeros
    print(resultado)
    
multiplos(2,2,2,2,2,2,2,2,2,2,2)'''

def par_impar(x):
    if x % 2 == 0:
        return print(f"{x} é par")
    
    return print(f"{x} é impar")
    
par_impar(11)