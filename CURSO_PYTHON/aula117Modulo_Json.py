import json
pessoa = {
  "nome": "Luiz Otávio 2",
  "sobrenome": "Miranda",
  "enderecos": [
    {
      "rua": "R1",
      "numero": 32
    },
    {
      "rua": "R2",
      "numero": 55
    }
  ],
  "altura": 1.8,
  "numeros_preferidos": (2, 3, 4, 5, 6),
  'dev': True,
  'nada': None,
}

with open('aula117.json', 'w', encoding='utf8') as arquivo: #usando o modulo with open e 'w' para criar um arquivo (importamos o json antes de criar o arquivo)
    json.dump(# Criando um arquivo com modulo json
        pessoa, 
        arquivo, 
        indent=2 #Usamos indent para organizar os dados
        )

with open('aula117.json', 'r', encoding='utf8') as arquivo: 
    pessoa = json.load(arquivo) #para retornar com o arquivo para python, basta usar o 'load' do arquivo
    print(pessoa)