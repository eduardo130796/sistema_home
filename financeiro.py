import streamlit as st
from ui import inject_css, header

def financeiro():
    inject_css()
    header("Financeiro", "Controle de receitas e despesas")

    tipo = st.selectbox("Tipo", ["Receita", "Despesa"])
    valor = st.number_input("Valor", 0.0)
    categoria = st.text_input("Categoria")
    st.date_input("Data")

    st.button("Salvar")

    st.markdown("### Movimentações")
    st.dataframe({
        "Tipo": ["Receita", "Despesa"],
        "Valor": [2500, 300],
        "Categoria": ["Pedido 101", "Material"],
        "Data": ["2025-11-01", "2025-11-02"]
    })
