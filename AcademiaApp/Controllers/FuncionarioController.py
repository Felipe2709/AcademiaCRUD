import sqlite3
from Models.Funcionario import Funcionario

def conectar():
    return sqlite3.connect(db_path)

def incluirFuncionario(funcionario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO funcionario (CPF, cargo, salario, data_admissao, nome, telefone, endereco) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (funcionario.getCPF(), funcionario.getCargo(), funcionario.getSalario(), funcionario.getDataAdmissao(),
                    funcionario.getNome(), funcionario.getTelefone(), funcionario.getEndereco()))
    conn.commit()
    conn.close()

def consultarFuncionarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionario")
    dados = cursor.fetchall()
    conn.close()
    return dados
