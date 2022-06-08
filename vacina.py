class Vacina:
    def __init__(self, id_vacina, nomeVacina, tipo, dose, disponibilidade):
        self._id_vacina = id_vacina
        self._nomeVacina = nomeVacina
        self._tipo = tipo
        self._dose = dose
        self._disponibilidade = disponibilidade
    
    
    @property
    def get_nome_vacina(self):
        return print(f"Nome da vacina: {self._nomeVacina}")

    @property
    def get_tipo(self):
        return print(f"Tipo da Vacina: {self._tipo}")

    @property
    def get_dose(self):
        return print(f"Dose: {self._dose}")

    @property
    def get_disponibilidade(self):
        return print(f"{self._disponibilidade} = verdade")

    @get_disponibilidade.setter
    def set_disponibilidade(self, disponibilidade):
        self._disponibilidade = disponibilidade



