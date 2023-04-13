# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'C:\\Users\\user\\Desktop\\Caminho da pasta\\' #Caminho onde quer criar o arquivo
caminho_arquivo += 'aula116.txt' #Arquivo que quer criar

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# with open(caminho_arquivo, 'w') as arquivo: #Usando o with o arquivo é fechado automaticamente
#     print('Olá, mundo')
#     print('Seu arquivo será fechado')

with open(caminho_arquivo, 'w') as arquivo: #Estamos escrendo no arquivo
    arquivo.write('Linha 1\r') #Para pular linha no windows, usa \r\n
    arquivo.write('Linha 2\r')
    arquivo.writelines(
        ('Linha 3\r', 'Linha 4\r') #Criando uma tupla com o que quero escrever
    )

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read()) #Aqui estamos lendo o arquivo inteiro

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: #Para ajustar os caracteres especiais de atenção (enconding='utf8')
    arquivo.write('Atenção\r') 
    arquivo.write('Linha 2\r')
    

   