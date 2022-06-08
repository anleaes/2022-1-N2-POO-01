class UnidadeSaude():
    def __init__(self, nome, endereco, telefone, cnpj):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cnpj = cnpj

    @property
    def get_nome(self):
        return self._nome

    @property
    def get_endereco(self):
        return self._endereco

    @property
    def get_telefone(self):
        return self._telefone

    @get_telefone.setter
    def set_telefone(self, telefone):
        self._telefone = telefone

    @property
    def get_cnpj(self):
        return self._cnpj

unidade1 = UnidadeSaude("Posto Modelo", "Av. Joao Pessoa", "32175004", "93.044.485-0001")

