from Models.Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, cpf, nome, telefone, endereco):
        super().__init__(cpf, nome, telefone, endereco)

    def getNomeCliente(self): return self.nome
