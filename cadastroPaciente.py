from pessoa import Pessoa

class CadastroPaciente(Pessoa):
        def __init__(self, nome, idade, telefone, cpf, email, endereco):
            super().__init__(nome, idade, telefone)
                self._cpf = cpf
                self._email = email
                self._endereco = endereco

        def validarCadastro(self, cpf):  
            if self._cpf == NULL and self._pessoa == NULL:
                print("Falha no cadastro. Por favor preencha o CPF!")
            else:
                print("Cadastro realizado com sucesso")