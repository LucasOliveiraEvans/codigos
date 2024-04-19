from randon import randint  


nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))
contador_regrecivo = 10
resultado = 0

for digito in nove_digitos:
    
    resultado += int(digito) * contador_regrecivo
    contador_regrecivo -= 1
    
resto = (resultado * 10) % 11

primeiro_digito = resto if resto <= 9 else 0


dez_digitos = nove_digitos + str(primeiro_digito)
contador_regrecivo_2 = 11

resultado_digito_2 = 0

for digito_2 in dez_digitos:
    
    resultado_digito_2 += int(digito_2) * contador_regrecivo_2
    contador_regrecivo_2 -= 1
    
resto_digito_2 = (resultado_digito_2 * 10) % 11

segundo_digito = resto_digito_2 if resto_digito_2 <= 9 else 0


cpf_completo = str(dez_digitos) + str(segundo_digito)
print(cpf_completo)
