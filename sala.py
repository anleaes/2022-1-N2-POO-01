
class Sala:
    def __init__(self, numero_sala, andar, unidade_saude):
        self._numero_sala = numero_sala
        self._andar = andar
        self._unidade_saude = unidade_saude

    def get_numeroSala(self):
        return self._numero_sala

    def get_andar(self):
        return self._andar

    def get_unidadeSaude(self):
        return self._unidade_saude

sala1 = Sala(1,2, "unidade1")
print(sala1.get_numeroSala())
print(sala1.get_andar())
print(sala1.get_unidadeSaude())