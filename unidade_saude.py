class UnidadeSaude():
    def __init__(self, nome, endereco, telefone, cnpj):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cnpj = cnpj

    def get_nome(self):
        return self._nome

unidade1 = UnidadeSaude("Posto Modelo", "Av. Joao Pessoa", "32175004", "93.044.485-0001")
