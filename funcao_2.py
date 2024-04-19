def soma(x,y):
    print(x + y)
    
    
    
soma(2,3)

#####################################


#função dentro de função

x = 1

def funcao():
    x = 10
    def funcao_interna():
        x = 11
        y = 2
        print(x,y)
        
    funcao_interna()
    print(x)
    
print(x)
funcao()
print(x)