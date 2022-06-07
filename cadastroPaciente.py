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

    def get_email(self):
        return self._email

    def get_endereco(self):
        return self._endereco


pc = CadastroPaciente(1234, "Rua tal, 122 ", "teste@teste.com", "thony", 28, "980631415")
print(pc)
print(pc.get_email())
print(pc.get_endereco())
