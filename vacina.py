class Vacina:
    def __init__(self, id_vacina, nomeVacina, tipo, dose, disponibilidade):
        self._id_vacina = id_vacina
        self._nomeVacina = nomeVacina
        self._tipo = tipo
        self._dose = dose
        self._disponibilidade = disponibilidade
    
    
    def get_nome_vacina(self):
        return self._nomeVacina

    def set_nome_vacina(self, nomeVacina):
        self._nomeVacina = nomeVacina

    def get_tipo(self):
        return self._tipo

    def get_dose(self):
        return self._dose

    def get_disponibilidade(self):
        return self._disponibilidade

    def set_nome_vacina(self, nomeVacina):
        self._nomeVacina = nomeVacina

    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_dose(self, dose):
        self._dose = dose

    def set_disponibilidade(self, disponibilidade):
        self._disponibilidade = disponibilidade

