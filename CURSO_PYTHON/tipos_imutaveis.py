"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool -> São considerados objetos, ou seja,você pode executar ações com esses objetos.
"""

string = 'Athana Silva'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)
print(string.zfill(10))
print(string.isspace())
print(string.lstrip('A'))

