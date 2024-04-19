import os
#criando arquivos com python
#usamos a função oopen para abrir
#um arquivo em python
#modos:
# r (read), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
#context manager - with (abre e fecha)
#Métodos úteis
#write, read (escrever e ler)
#writelines (escrever varias linhas)
#seek (move o cursor)
#readline (ler linha)
#readlines (ler linhas)
#módulo os:
#os.remove ou unlink - apaga arquivos
#os.rename - troca o nome ou move arquivo
#módulo json:
#json.dump = gera um arquivo json
#json.load


caminho_arquivo = 'arquivos.txt'

# arquivo = open(caminho_arquivo, 'w')
#
# arquivo.close()
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
    arquivo.write('atenção\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('lendo')
    arquivo.seek(0, 0)

    for linha in arquivo.readlines():
        print(linha.strip())
    
print('=' * 30)
    
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    print(arquivo.read())