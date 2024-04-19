from random import randint
dados = [randint(1,6) for i in range(100)]
dados.sort()
print(dados)
dadosRep = {}
for n in dados:
    dadosRep[n] = dadosRep.get(n,0) + 1
#Impressão do dicionário apenas com print
print(dadosRep)
#ou impressão passando um por um do dicionário
for n, qt in dadosRep.items():
    print(f'{n} apareceu {qt} vezes')