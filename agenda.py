from vacina import Vacina

class Agenda(Vacina):
    def __init__(self, hora, sala, vacina):
        super().__init__(vacina)
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
