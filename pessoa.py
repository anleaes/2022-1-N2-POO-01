class Pessoa:
    def __init__(self, nome, idade, telefone):
        self._nome = nome
        self._idade = idade
        self._telefone = telefone

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade
    
    def get_telefone(self):
        return self._telefone

    def set_nome(self, nome):
        self._nome = nome

    def set_idade(self, idade):
        self._idade = idade

    def set_telefone(self, telefone):
        self._telefone = telefone


