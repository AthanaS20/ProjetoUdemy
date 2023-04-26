class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        self.user = user
    # Podemos criar um metodo para definir o parametro apenas depois que o metodo for executado.

    def set_password(self, password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
         

# c1 = Connection()
c1 = Connection.create_with_auth('Athana', '1234')
# c1.set_user('Athana')
# c1.set_password('1234')
print(c1.user)
print(c1.password)
