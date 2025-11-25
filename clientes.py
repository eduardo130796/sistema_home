import streamlit as st
from ui import inject_css, header

def clientes():
    inject_css()
    header("Clientes", "Gerencie seus clientes")

    busca = st.text_input("Buscar cliente")

    st.markdown("### Cadastro de novo cliente")
    nome = st.text_input("Nome completo")
    telefone = st.text_input("Telefone")
    email = st.text_input("E-mail")
    cpf = st.text_input("CPF/CNPJ")
    endereco = st.text_area("Endereço")

    st.button("Salvar cliente")

    st.markdown("### Lista de clientes")
    st.dataframe({
        "Nome": ["Maria", "João", "Carlos"],
        "Telefone": ["99999-1111", "98888-2222", "97777-3333"],
        "CPF/CNPJ": ["000.000.000-00", "111.111.111-11", "222.222.222-22"]
    })
