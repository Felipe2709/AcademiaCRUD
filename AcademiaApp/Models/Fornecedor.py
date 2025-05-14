class Fornecedor:
    def __init__(self, idFornecedor, nome, telefone, endereco, cnpj):
        self.idFornecedor = idFornecedor
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cnpj = cnpj

    def getIdFornecedor(self): return self.idFornecedor
    def getNomeFornecedor(self): return self.nome
    def getTelefone(self): return self.telefone
    def getEndereco(self): return self.endereco
    def getCNPJ(self): return self.cnpj
