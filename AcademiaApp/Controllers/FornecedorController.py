import sqlite3
from Models.Fornecedor import Fornecedor

def conectar():
    return sqlite3.connect(db_path)

def incluirFornecedor(fornecedor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO fornecedor (id_fornecedorPK, nome_fornecedor, telefone, endereco, CNPJ) VALUES (?, ?, ?, ?, ?)",
                   (fornecedor.getIdFornecedor(), fornecedor.getNomeFornecedor(), fornecedor.getTelefone(), fornecedor.getEndereco(), fornecedor.getCNPJ()))
    conn.commit()
    conn.close()

def consultarFornecedores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fornecedor")
    dados = cursor.fetchall()
    conn.close()
    return dados
