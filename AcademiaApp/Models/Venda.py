class Venda:
    def __init__(self, idVenda, idFuncionario, valorTotal, dataVenda):
        self.idVenda = idVenda
        self.idFuncionario = idFuncionario
        self.valorTotal = valorTotal
        self.dataVenda = dataVenda

    def getIdVenda(self): return self.idVenda
    def getIdFuncionario(self): return self.idFuncionario
    def getValorTotal(self): return self.valorTotal
    def getDataVenda(self): return self.dataVenda
