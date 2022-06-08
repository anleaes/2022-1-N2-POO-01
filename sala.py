from unidade_saude import UnidadeSaude
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

    def set_numeroSala(self, numero_sala):
        self._numero_sala = numero_sala

    def set_andar(self, andar):
        self._andar = andar

    def set_unidadeSaude(self, unidade_saude):
        self._unidade_saude = unidade_saude
        




