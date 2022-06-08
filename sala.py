from unidade_saude import UnidadeSaude

class Sala:
    def __init__(self, numero_sala, andar, unidade_saude):
        self._numero_sala = numero_sala
        self._andar = andar
        self._unidade_saude = unidade_saude
        
    @property
    def get_numero_sala(self):
        return print(f"Numero da sala: {self._numero_sala}")

    @property
    def get_andar(self):
        return print(f"Andar: {self._andar}")

   



        




