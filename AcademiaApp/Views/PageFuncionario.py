import streamlit as st
import Controllers.FuncionarioController as controller
from Models.Funcionario import Funcionario
from datetime import date

def show_funcionario_page():
    st.title("Cadastro de Funcionário")
    cpf = st.text_input("CPF")
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    endereco = st.text_input("Endereço")
    cargo = st.text_input("Cargo")
    salario = st.number_input("Salário", min_value=0.0)
    dataAdmissao = st.date_input("Data de Admissão", value=date.today())

    if st.button("Cadastrar Funcionário"):
        funcionario = Funcionario(cpf, nome, telefone, endereco, cargo, salario, dataAdmissao)
        controller.incluirFuncionario(funcionario)
        st.success("Funcionário cadastrado com sucesso!")

    if st.button("Consultar Funcionários"):
        dados = controller.consultarFuncionarios()
        st.table(dados)
