'''
funções (def) em python
funções são trechos de código usados para
replicar determinadas ações ao longo do seu código
elas podem receber valores para parâmetros (argumentos)
e retornar um valor especifico
'''

#def multiplos(x,y):
#    print(f"{x} é divisivel por {y}?")
#    resultado = (x % y) == 0
#    print(resultado)
#
#    
#multiplos(18,9)
#multiplos(20,5)
#multiplos(13,7)

def saudacao(saudamento,nome):
    print(f'{saudamento}, {nome}')
    
saudacao('bom dia','roberto')