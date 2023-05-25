from log import LogFileMixin, LogPrintMixin

l = LogPrintMixin()
l.log_error('qualquer coisa')
l.log_sucess('Log realizado com sucesso.')
lf = LogFileMixin()
lf.log_error('qualquer coisa')
lf.log_sucess('Log realizado com sucesso.')
