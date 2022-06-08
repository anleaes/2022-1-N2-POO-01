from sala import Sala
from vacina import Vacina

class Agenda():
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
   
    def agendar_vacina(self):
        if self._vacina is not False:
            return print(f'Vacina {self._vacina} disponivel para o dia ...')
        else:
            return print(f'A vacina não está disponível no momento.')

sala1 = Sala(10, 2, "unidade1")
vacina1 = Vacina(180, "Clozapina", "viral", "dose unica", True)
agenda1 = Agenda("10:30", "08/06", sala1, vacina1)

