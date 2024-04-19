def fat_soma(fat):
    if fat == 1:
        return fat
    else:
        return fat * fat_soma(fat - 1)


fat=int(input('digite o numero desejado:'))
print('o fatorial de {} é {}'.format(fat,fat_soma(fat)))