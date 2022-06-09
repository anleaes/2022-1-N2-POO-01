from cadastroPaciente import CadastroPaciente
from agenda import Agenda
from sala import Sala
from vacina import Vacina
from unidade_saude import UnidadeSaude
from enfermeiro import Enfermeiro

class MarcacaoVacina:
    def __init__(self, idMarcacao, cadastro_paciente, agenda, enfermeiro):
       self._idMarcacao = idMarcacao
       self._cadastro_paciente = cadastro_paciente
       self._agenda = agenda
       self._enfermeiro = enfermeiro

    def get_id(self):
        return print(f"ID: {self._idMarcacao}")

    def validar_paciente(self, cadastro_paciente):
        if self._cadastro_paciente == cadastro_paciente:
            print("Validação efetuada!")
        else:
            print("Dados incompativeis")
    
    def agendar_vacina(self):
        hora = agenda1._hora
        data = agenda1._data
        nomeEnf = enf._nome 
        regEnf = enf._registro
        vac = agenda1._vacina._nomeVacina
        vacTipo = agenda1._vacina._tipo
        vacDose = agenda1._vacina._dose
        print(f"Vacina agendada para:\nDATA: {data}\nHORA: {hora}")
        print()
        print(f"Enfermeiro: {nomeEnf}\nRegistro: {regEnf}")
        print()
        print(f"Vacina: {vac}\nTipo:{vacTipo}\nDose: {vacDose}")
        
#Objetos instanciados para execução do codigo
cPaciente =  CadastroPaciente("03232588409", "Poa", "teste@teste.com", "Josiclei Judison", 30, "32178009")
enf= Enfermeiro(102, "thony", 28, "980546478")
unidade1 = UnidadeSaude("Posto Modelo", "Av. Joao Pessoa", "32175004", "93.044.485-0001")
sala1 = Sala(10, 2, unidade1)
vacina1 = Vacina(180, "Clozapina", "viral", "dose unica", True)
agenda1 = Agenda("10:30", "08/06/2022", sala1, vacina1)
Mconsulta = MarcacaoVacina(10, cPaciente, agenda1, enf)

#execução dos metodos
Mconsulta.validar_paciente(cPaciente)
print()
Mconsulta._agenda._sala.get_andar
Mconsulta._agenda.get_informar_data
Mconsulta._agenda.get_informar_horario
Mconsulta._agenda._sala.get_numero_sala
print()
Mconsulta.agendar_vacina()