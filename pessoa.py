class Pessoa:
    def __init__(self, nome, idade, telefone):
        self._nome = nome
        self._idade = idade
        self._telefone = telefone

    @property
    def get_nome(self):
        return print(f"Nome: {self._nome}")

    @get_nome.setter
    def set_nome(self, nome):
        self._nome = nome

    @property
    def get_idade(self):
        return print(f"Idade: {self._idade}")

    @get_idade.setter
    def set_idade(self, idade):
        self._idade = idade

    @property
    def get_telefone(self):
        return print(f"Telefone: {self._telefone}")

    @get_telefone.setter
    def set_telefone(self, telefone):
        self._telefone = telefone


