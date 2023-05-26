# Abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
# Para buscar o caminho desse arquivo (aula_144)

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = (f'{msg} {self.__class__.__name__}')
        print(f'Salvando no log')
        with open (LOG_FILE, 'a') as arquivo: # Criando arquivo log.txt
            arquivo.write(msg_formatada)
            arquivo.write('\n')

if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('qualquer coisa')
    l.log_sucess('Log realizado com sucesso.')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_sucess('Log realizado com sucesso.')
    