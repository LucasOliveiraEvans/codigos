def fiboter(termo):
    if termo<=2:
        return 1
    else:
        return fiboter(termo-1) + fiboter(termo-2)
                        
                        
termo=int(input('digite o termo desejado:'))
print('o {} termo da sequencia é {}'.format(termo,fiboter(termo)))