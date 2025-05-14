import streamlit as st
import sys
from pathlib import Path
import importlib

st.set_page_config(page_title="Sistema de Academia", layout="wide", initial_sidebar_state="auto")

sys.path.append(str(Path(__file__).parent))

PAGES = {
    "Cliente": "Views.PageCliente",
    "Funcionário": "Views.PageFuncionario",
    "Produto": "Views.PageProduto",
    "Venda": "Views.PageVenda",
    "Fornecedor": "Views.PageFornecedor"
}

def load_page(page_name):
    try:
        module = importlib.import_module(PAGES[page_name])
        page_name_clean = page_name.lower().replace("á", "a").replace("ç", "c")
        return getattr(module, f"show_{page_name_clean}_page")
    except (ImportError, AttributeError, KeyError) as e:
        st.error(f"Erro ao carregar a página {page_name}: {e}")
        st.warning("Entre em contato com o administrador do sistema.")
        return None

def main():
    st.title('Sistema de Cadastro da Academia')

    with st.sidebar:
        st.title("Menu")
        page_selection = st.selectbox("Selecione uma opção", list(PAGES.keys()))

    show_page = load_page(page_selection)
    if show_page:
        show_page()

if __name__ == "__main__":
    main()
