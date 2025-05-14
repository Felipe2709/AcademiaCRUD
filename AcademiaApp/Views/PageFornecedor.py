import streamlit as st
import Controllers.FornecedorController as controller
from Models.Fornecedor import Fornecedor

def show_fornecedor_page():
    st.title("Cadastro de Fornecedor")
    id_fornecedor = st.number_input("ID Fornecedor", min_value=1)
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    endereco = st.text_input("Endereço")
    cnpj = st.text_input("CNPJ")

    if st.button("Cadastrar Fornecedor"):
        fornecedor = Fornecedor(id_fornecedor, nome, telefone, endereco, cnpj)
        controller.incluirFornecedor(fornecedor)
        st.success("Fornecedor cadastrado com sucesso!")

    if st.button("Consultar Fornecedores"):
        dados = controller.consultarFornecedores()
        st.table(dados)
