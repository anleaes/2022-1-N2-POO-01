from sala import Sala
from vacina import Vacina

class Agenda:
    def __init__(self, hora, data, sala, vacina):
        self._hora = hora
        self._data = data
        self._sala = sala
        self._vacina = vacina
        
    @property
    def get_informar_horario(self):
        return print(f" Hora: {self._hora}")

    @get_informar_horario.setter
    def set_horario(self, hora):
        self._hora = hora
        
    @property
    def get_informar_data(self):
        return print(f" Hora: {self._data}")

    @get_informar_horario.setter
    def set_data(self, data):
        self._data = data
    

sala1 = Sala(10, 2, "unidade1")
vacina1 = Vacina(180, "Clozapina", "Viral", "dose unica", True)
agenda1 = Agenda("10:30", "08/06/2022", sala1, vacina1)

agenda1.get_informar_data
agenda1.get_informar_horario
agenda1._sala.get_andar
agenda1._sala.get_numero_sala
agenda1._vacina.get_nome_vacina
agenda1._vacina.get_tipo
agenda1._vacina.get_dose
agenda1._vacina.get_disponibilidade