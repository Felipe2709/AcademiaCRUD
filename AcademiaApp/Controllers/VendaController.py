import sqlite3
from Models.Venda import Venda

def conectar():
    return sqlite3.connect(db_path)

def incluirVenda(venda):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vendas (id_vendaPK, id_funcionarioFK, valorTotal, dataVenda) VALUES (?, ?, ?, ?)",
                   (venda.getIdVenda(), venda.getIdFuncionario(), venda.getValorTotal(), venda.getDataVenda()))
    conn.commit()
    conn.close()

def consultarVendas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendas")
    dados = cursor.fetchall()
    conn.close()
    return dados
