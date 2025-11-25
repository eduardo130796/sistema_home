import streamlit as st
from ui import inject_css, header

def area_cliente():
    inject_css()
    header("Área do Cliente")

    cpf = st.text_input("CPF/CNPJ")
    pedido = st.text_input("Número do pedido")

    st.button("Consultar")

    st.markdown("### Status do pedido")
    st.info("Em produção")
