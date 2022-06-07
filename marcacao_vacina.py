from cadastroPaciente import CadastroPaciente
from agenda import Agenda

class MarcacaoVacina(CadastroPaciente, Agenda):
    def __init__(self, idMarcacao):
       self._idMarcacao = idMarcacao

    def get_id(self):
        return self._idMarcacao

