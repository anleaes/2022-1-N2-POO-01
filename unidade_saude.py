class UnidadeSaude():
    def __init__(self, nome, endereco, telefone, cnpj):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cnpj = cnpj

unidade1 = UnidadeSaude("Posto Modelo", "Av. Joao Pessoa", "32175004", "93.044.485-0001")