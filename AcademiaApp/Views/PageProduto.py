import streamlit as st
import Controllers.ProdutoController as controller
from Models.Produto import Produto

def show_produto_page():
    st.title("Cadastro de Produto")
    id_produto = st.number_input("ID Produto", min_value=1)
    descricao = st.text_input("Descrição")
    preco_venda = st.number_input("Preço Venda", min_value=0.0)
    preco_custo = st.number_input("Preço Custo", min_value=0.0)
    estoque = st.number_input("Estoque", min_value=0)
    id_fornecedor = st.number_input("ID Fornecedor", min_value=1)
    categoria = st.text_input("Categoria")

    if st.button("Cadastrar Produto"):
        produto = Produto(id_produto, descricao, preco_venda, preco_custo, estoque, id_fornecedor, categoria)
        controller.incluirProduto(produto)
        st.success("Produto cadastrado com sucesso!")

    if st.button("Consultar Produtos"):
        dados = controller.consultarProdutos()
        st.table(dados)
