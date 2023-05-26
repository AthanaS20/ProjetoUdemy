# from log import LogFileMixin, LogPrintMixin

# l = LogPrintMixin()
# l.log_error('qualquer coisa')
# l.log_sucess('Log realizado com sucesso.')
# lf = LogFileMixin()
# lf.log_error('qualquer coisa')
# lf.log_sucess('Log realizado com sucesso.')

from eletronico import Smartphone

galaxy = Smartphone('Galaxy 20')
iphone = Smartphone('Iphone 13')

galaxy.desligando()
iphone.ligando()

