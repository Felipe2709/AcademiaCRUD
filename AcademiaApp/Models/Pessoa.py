class Pessoa:
    def __init__(self, cpf, nome, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def getCPF(self): return self.cpf
    def getNome(self): return self.nome
    def getTelefone(self): return self.telefone
    def getEndereco(self): return self.endereco
