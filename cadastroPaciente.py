from pessoa import Pessoa

class CadastroPaciente(Pessoa):
    def __init__(self, cpf, endereco, email, nome, idade, telefone):
        super().__init__(nome, idade, telefone)
        self._cpf = cpf
        self._email = email
        self._endereco = endereco

    def validarCadastro(self, cpf):  
        if self._cpf != cpf : 
            print("Falha no cadastro. Por favor preencha o CPF!")
        else:
            print("Cadastro realizado com sucesso")

    @property
    def get_email(self):
        return print(f"Email: {self._email}")
    
    @get_email.setter
    def set_email(self, email):
        self._email = email

    @property
    def get_endereco(self):
        return print(f"Endereço: {self._endereco}")

    @get_endereco.setter
    def set_endereco(self, endereco):
        self._endereco = endereco


