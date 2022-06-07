from pessoa import Pessoa

class Enfermeiro(Pessoa):
    def __init__(self, registro, nome, idade, telefone):
        super().__init__(nome, idade, telefone)
        self._registro = registro

    def get_registro(self):
        return self._registro

    def set_registro(self, registro):
        self._registro = registro


enf= Enfermeiro(102, "thony", 28, "980546478")
print(enf)
print(enf.get_registro())
enf.set_registro(104)
print(enf.get_registro())