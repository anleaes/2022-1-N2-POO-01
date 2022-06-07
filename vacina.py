class Vacina:
    def __init__(self, id_vacina, nomeVacina, tipo, dose, disponibilidade):
        self._id_vacina = id_vacina
        self._nomeVacina = nomeVacina
        self._tipo = tipo
        self._dose = dose
        self._disponibilidade = disponibilidade
    
    @property
    def get_nome_vacina(self):
        return self._nomeVacina

    @property
    def set_nome_vacina(self, nomeVacina):
        self._nomeVacina = nomeVacina

v1 = Vacina(1, "Vacina Pasrao", "viral", "dose unica", True)