#map - para mapear dados
from functools import partial


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

def aumentar_preco(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumentar_preco, porcentagem=1.1)

# novos_produtos = [
#     {**p, 'preco': aumentar_preco(p['preco'])} for p in produtos
# ]

def muda_preco(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}
novos_produtos = map(muda_preco, produtos)

print_iter(produtos)
print_iter(novos_produtos)