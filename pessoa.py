class Pessoa:
    def __init__(self, nome, idade, telefone):
        self._nome = nome
        self._idade = idade
        self._telefone = telefone

    def get_nome(self):
        return self._nome

p1 = Pessoa("Marco", 25, "980465784")
print(p1.get_nome())