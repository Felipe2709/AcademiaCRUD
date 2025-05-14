import streamlit as st
import Controllers.ClienteController as controller
from Models.Cliente import Cliente

def show_cliente_page():
    st.title("Cadastro de Cliente")
    cpf = st.text_input("CPF")
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    endereco = st.text_input("Endereço")

    if st.button("Cadastrar Cliente"):
        cliente = Cliente(cpf, nome, telefone, endereco)
        controller.incluirCliente(cliente)
        st.success("Cliente cadastrado com sucesso!")

    if st.button("Consultar Clientes"):
        dados = controller.consultarClientes()
        st.table(dados)
