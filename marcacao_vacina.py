from cadastroPaciente import CadastroPaciente
from agenda import Agenda

class MarcacaoVacina:
    def __init__(self, idMarcacao, cadastro_paciente, agenda):
       self._idMarcacao = idMarcacao
       self._cadastro_paciente = cadastro_paciente
       self._agenda = agenda

    def get_id(self):
        return self._idMarcacao

    

