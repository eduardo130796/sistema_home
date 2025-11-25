import streamlit as st
from ui import inject_css, header

def produtos():
    inject_css()
    header("Produtos", "Cadastre e gerencie produtos")

    nome = st.text_input("Nome do produto")
    tipo = st.selectbox("Tipo de cálculo", ["Unidade", "m²"])
    valor = st.number_input("Valor unitário", min_value=0.0, step=0.01)

    st.button("Salvar produto")

    st.markdown("### Lista de produtos")
    st.dataframe({
        "Produto": ["Adesivo", "Placa PVC", "Banner"],
        "Tipo": ["m²", "unidade", "m²"],
        "Valor": [50, 30, 40]
    })
