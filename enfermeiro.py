from pessoa import Pessoa

class Enfermeiro(Pessoa):
    def __init__(self, registro, nome, idade, telefone):
        super().__init__(nome, idade, telefone)
        self._registro = registro

enf= Enfermeiro(102, "thony", 28, "980546478")