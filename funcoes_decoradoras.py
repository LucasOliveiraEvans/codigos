#funções decoradoras e decoradores
#decorar = adicionar/remover/restringir/alterar
#funções decoradoras são funções que decoram outras funções
#decoradores são usados para fazer o python
#usar as funções decoradoras em outras funções.
#decoradores são "Syntax Sugar" (açúcar sintático)

def criar_funcao(func):
    def interna(*args,**kwargs):
        print("vou decorar")
        resultado = func(*args,**kwargs)
        print(f'o seu resultado foi {resultado}')
        print('você foi decorado')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

invertendo_strings = criar_funcao(inverte_string)
invertida = invertendo_strings('123')
print(invertida)