import streamlit as st
import Controllers.VendaController as controller
from Models.Venda import Venda
from datetime import date

def show_venda_page():
    st.title("Cadastro de Venda")
    id_venda = st.number_input("ID Venda", min_value=1)
    id_funcionario = st.number_input("ID Funcionário", min_value=1)
    valor_total = st.number_input("Valor Total", min_value=0.0)
    data_venda = st.date_input("Data da Venda", value=date.today())

    if st.button("Cadastrar Venda"):
        venda = Venda(id_venda, id_funcionario, valor_total, data_venda)
        controller.incluirVenda(venda)
        st.success("Venda cadastrada com sucesso!")

    if st.button("Consultar Vendas"):
        dados = controller.consultarVendas()
        st.table(dados)
