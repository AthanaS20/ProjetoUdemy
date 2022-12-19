"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 40:
    contador += 1
    

    if contador == 6: # Se quiser interromper em determinado valor ou situação
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        continue
    print(contador)

# continue -> é usado para ignorar ou pular a sequencia

