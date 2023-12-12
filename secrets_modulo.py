# secrets gera números aleatórios seguros

# import string as s
# from secrets import SystemRandom as Sr

# print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"

import secrets
import string as s
from secrets import SystemRandom as Sr 

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12))) # criando uma senha aleatoria



random = secrets.SystemRandom()

# lista = ['Ana', 'Patricia', 'Amanda']
# random.shuffle(lista)
# print(lista)
