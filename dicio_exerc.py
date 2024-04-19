perguntas = [
    {
        'pergunta':'quanto é 2+2?',
        'opções':['1','3','4','5'],
        
    },
    {
        'pergunta':'quanto é 5*5?',
        'opções':['25','55','10','51'],
        
    },
    {
        'pergunta':'quanto é 10/2?',
        'opções':['1','2','4','5'],
        
    }
]
while True:
    acerto = 0
    erro = 0
    print(perguntas[0])
    resposta1 = int(input('digite uma opção: '))
    if resposta1 == 4:
        print('ACERTOU!')
        acerto += 1
    else:
        print('ERROU!')
        erro += 1
    print(perguntas[1])
    resposta2 = int(input('digite uma opção: '))
    if resposta2 == 25:
        print('ACERTOU!')
        acerto += 1
    else:
        print('ERROU!')
        erro += 1
    print(perguntas[2])
    resposta3 = int(input('digite uma opção: '))
    if resposta3 == 5:
        print('ACERTOU!')
        acerto += 1
    else:
        print('ERROU!')
        erro += 1
    print('você terminou,parabens!')
    print(f'você acertou {acerto} perguntas e errou {erro}')
    break
    