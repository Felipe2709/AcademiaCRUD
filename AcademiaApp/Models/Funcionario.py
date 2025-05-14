from Models.Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, cpf, nome, telefone, endereco, cargo, salario, dataAdmissao):
        super().__init__(cpf, nome, telefone, endereco)
        self.cargo = cargo
        self.salario = salario
        self.dataAdmissao = dataAdmissao

    def getCargo(self): return self.cargo
    def getSalario(self): return self.salario
    def getDataAdmissao(self): return self.dataAdmissao
