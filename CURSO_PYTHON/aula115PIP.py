print('OI')

# Caso você precise importar o seu código para um repositório sem precisa copiar toda a pasta
# venv (geralmente é muito grande, devido aos pacotes instalados), basta criar o arquivo
# requirements.txt, que salva todos os pacotes instalados na sua venv.

#Comando: pip freeze > requirements.txt

# Caso apague a pasta venv e queira criar de novo com os pacotes anteriores, basta
# criar o ambiente virtual, ativar e depois digitar o comando:
# pip install -r .\requirements.txt

# Conforme for instalando pacotes no ambiente virtual, é necessário atualizar o requirements.txt
# basta fazer o mesmo comando: pip freeze > requirements.txt