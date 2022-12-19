"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

quantidade_de_linhas = 5
quantidade_de_colunas = 5

linha = 1

while linha <= quantidade_de_linhas: # Esse é o while principal, sem essa condição a debaixo não pode ser realizada
    
    coluna = 1
    while coluna <= quantidade_de_colunas: # o while pode ser usado dentro do outro para executar outro loop
        print(linha, coluna)
        coluna += 1 
        

    

    linha += 1

print('Acabou')