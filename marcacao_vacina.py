from cadastroPaciente import CadastroPaciente
from agenda import Agenda
from vacina import Vacina

class MarcacaoVacina(CadastroPaciente, Agenda, Vacina):
    def __init__(self, idMarcacao, cadastroPaciente, agenda):
        CadastroPaciente.__init__(self, cpf, email, endereco, pessoa)
        Agenda.__init__(self, hora, sala, Vacina)
        Vacina.__init__(self, id_vacina,nomeVacina,tipo, dose, disponibilidade, Agenda)
        self._idMarcacao = idMarcacao

    def get_id(self):
        return self._idMarcacao