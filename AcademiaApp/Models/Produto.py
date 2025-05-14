class Produto:
    def __init__(self, idProduto, descricao, precoVenda, precoCusto, estoque, fornecedorId, categoria):
        self.idProduto = idProduto
        self.descricao = descricao
        self.precoVenda = precoVenda
        self.precoCusto = precoCusto
        self.estoque = estoque
        self.fornecedorId = fornecedorId
        self.categoria = categoria

    def getIdProduto(self): return self.idProduto
    def getDescricao(self): return self.descricao
    def getPrecoVenda(self): return self.precoVenda
    def getPrecoCusto(self): return self.precoCusto
    def getEstoque(self): return self.estoque
    def getFornecedorId(self): return self.fornecedorId
    def getCategoria(self): return self.categoria
