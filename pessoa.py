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

p1 = Pessoa("Marco", 25, "980465784")
print(p1)
print(p1.get_nome())
print(p1.get_idade())
print(p1.get_telefone())

print('------------------------')
print('')

p1.set_nome('Thony')
print(p1.get_nome())