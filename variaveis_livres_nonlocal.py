#nesse exercicio a variavel valor_final é a variavel livre
#pois não está definida na função de dentro, no caso a função "interna"

def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c())
print(c('b'))
print(c('c'))
print(c('d'))