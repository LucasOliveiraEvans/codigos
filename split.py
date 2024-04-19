'''
split: quebra a string dependendo de qual caractere foi passado
'''

frase= 'olha só que, coisa interesante'
lista_frases= frase.split(',')



for i,frase in enumerate(lista_frases):
    print(lista_frases[i].strip())

'''
strip:corta os espaços no começo e no fim (no caso acima o espço antes
da palabra 'coisa' seria cortado e não existiria,porém não altera a lista)
'''
'''
join: une strings
'''

frase_join = '-'.join('abc')
print(frase_join)