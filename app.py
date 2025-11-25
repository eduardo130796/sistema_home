import streamlit as st
from dashboard import dashboard
from clientes import clientes
from produtos import produtos
from orcamentos import orcamentos
from pedidos import pedidos
from producao import producao
from financeiro import financeiro
from area_cliente import area_cliente

st.sidebar.title("Menu")

pagina = st.sidebar.radio("Navegar para:", [
    "Dashboard",
    "Clientes",
    "Produtos",
    "Orçamentos",
    "Produção",
    "Financeiro",
    "Área do Cliente"
])

if pagina == "Dashboard":
    dashboard()
elif pagina == "Clientes":
    clientes()
elif pagina == "Produtos":
    produtos()
elif pagina == "Orçamentos":
    orcamentos()
elif pagina == "Produção":
    producao()
elif pagina == "Financeiro":
    financeiro()
else:
    area_cliente()
