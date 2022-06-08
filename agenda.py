from sala import Sala
from vacina import Vacina
from unidade_saude import UnidadeSaude

class Agenda():
    def __init__(self, hora, sala, vacina):
        self._hora = hora
        self._sala = sala
        self._vacina = vacina
        
    @property
    def get_verificar_horario(self):
        return self._hora

    @get_verificar_horario.setter
    def set_horario(self, hora):
        self._hora = hora

    @property
    def get_verificar_sala(self):
        return self._sala

    @get_verificar_sala.setter
    def set_sala(self, sala):
        self._sala = sala

    def agendar_vacina(self):
        if self._vacina is not False:
            return print(f'Vacina {self._vacina} disponivel para o dia ...')
        else:
            return print(f'A vacina não está disponível no momento.')





