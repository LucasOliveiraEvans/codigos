'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao},{nome}!'
    return saudar

bom_dia= criar_saudacao('bom dia')
boa_noite= criar_saudacao('boa noite')

print(bom_dia('luiz'))
print(boa_noite('carlos'))

'''fazendo dessa forma, a função maior recebe o valor da primeira variavel
e lembra dele pois assim adia a execução da função saudar,assim a saudacao1
contem o valor da criar_saudacao(o mesmo se aplica a saudacao2).
para que assim quando for passado o segundo parametro (no caso o nome) a
segunda função é finalmente utilizada,guardando a saudacao e o nome na variavel
'''

#caso precise de uma lista com varios nomes podemos fazer um for

for nome in ['maria','bruna','kleber']:
    print(bom_dia(nome))
    print(boa_noite(nome))