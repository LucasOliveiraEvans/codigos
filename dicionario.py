agenda = {'Ana Elisa':'9999', 'Beatriz':'87787', 'Daniel': '555'}
print(agenda)
if 'Ana' in agenda:
    print(agenda['Ana'])
else:
    print('Nome não cadastrado')

print(agenda)
print(agenda.keys())
print(agenda.values())
print(agenda.items())

#Percorrendo um dicionário
for nome, celular in agenda.items():
    print(nome, celular)

#Inserindo no dicionário
agenda['Daniel'] = '877667'
agenda['Carlos'] = '6666'
print(agenda)