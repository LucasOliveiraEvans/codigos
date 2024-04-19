def produto(base,expo):
    if expo==0:
        return 1
    else:
        return base * produto(base,expo-1)



base=int(input('digite a base:'))
expo=int(input('digite o expoente:'))
print(produto(base,expo))