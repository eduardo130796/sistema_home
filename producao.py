import streamlit as st
from ui import inject_css, header

def producao():
    inject_css()
    header("Produção", "Fila de pedidos para produção")

    st.dataframe({
        "Pedido": [101, 102],
        "Cliente": ["Maria", "João"],
        "Produto": ["Adesivo", "Banner"],
        "Status": ["Em produção", "Em produção"]
    })

    st.button("Marcar como finalizado")
