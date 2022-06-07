from sala import Sala
from vacina import Vacina
from unidade_saude import UnidadeSaude
class Agenda:
    def __init__(self, hora, sala, vacina):
        self._hora = hora
        self._sala = sala
        self._vacina = vacina
        
    def verificar_agenda(self):
        print(self._hora)
        print(self._sala)

    def agendar_vacina(self):
        if self._vacina is not False:
            return print(f'Vacina {self._vacina} disponivel para o dia ...')
        else:
            return print(f'A vacina não está disponível no momento.')

    def get_horario(self):
        return self._hora

    def set_horario(self, hora):
        self._hora = hora

unidade1 = UnidadeSaude("Posto Modelo", "Av. Joao Pessoa", "32175004", "93.044.485-0001")
sala1 = Sala(10, 2, unidade1)
vacina1 = Vacina(180, "Clozapina", "viral", "dose unica", True)
agenda1 = Agenda("10:30", sala1, vacina1)


