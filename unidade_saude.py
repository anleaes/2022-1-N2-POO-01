class UnidadeSaude():
    def __init__(self, nome, endereco, telefone, cnpj):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cnpj = cnpj

    def get_nome(self):
        return self._nome

    def get_endereco(self):
        return self._endereco

    def get_telefone(self):
        return self._telefone

    def get_cnpj(self):
        return self._cnpj

    def set_nome(self, nome):
        self._nome = nome

    def set_telefone(self, telefone):
        self._telefone = telefone



