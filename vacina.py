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

v1 = Vacina(1, "Vacina Pasrao", "viral", "dose unica", True)