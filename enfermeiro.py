from pessoa import Pessoa

class Enfermeiro(Pessoa):
    def __init___(self, registro, nome, idade, telefone):
        super().__init__(nome, idade, telefone)
        self._registro = registro

    
