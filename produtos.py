import copy
produtos = [
    {'nome':'produto 5','preco':10.00},
    {'nome':'produto 1','preco':22.32},
    {'nome':'produto 3','preco':10.11},
    {'nome':'produto 2','preco':105.87},
    {'nome':'produto 4','preco':69.90},
]

#produtos 10% mais caros
novos_produtos = [
    {**p,'preco': round(p['preco'] * 1.1, 2)}   
    for p in copy.deepcopy(produtos)
]
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')


#produtos por ordem decrescente
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print()
print(*produtos_ordenados_por_nome, sep='\n')


#preço do menor para o maior
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)


print()
print(*produtos_ordenados_por_preco, sep='\n')