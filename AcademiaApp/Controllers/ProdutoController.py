import sqlite3
from Models.Produto import Produto

def conectar():
    return sqlite3.connect(db_path)

def incluirProduto(produto):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (id_produtoPK, descricao, preco_venda, preco_custo, qt_estoque, id_fornecedorFK, categoria) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (produto.getIdProduto(), produto.getDescricao(), produto.getPrecoVenda(), produto.getPrecoCusto(),
                    produto.getEstoque(), produto.getFornecedorId(), produto.getCategoria()))
    conn.commit()
    conn.close()

def consultarProdutos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    dados = cursor.fetchall()
    conn.close()
    return dados
