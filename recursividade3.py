def exp (base, expo):
    if expo == 0:
        return 1
    return base * exp(base, expo-1)

print("Informe a base e o expoente")
b = int(input("Base: "))
e = int(input("Expoente: "))
if e < 0:
    print("O expoente não pode ser negativo")
else:
    print(exp(b,e))