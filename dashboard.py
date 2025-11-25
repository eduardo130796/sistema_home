import streamlit as st
from ui import inject_css, header, card

def dashboard():
    inject_css()
    header("Dashboard", "Visão geral do sistema")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        card("Orçamentos do mês", "48")
    with col2:
        card("Pedidos", "27")
    with col3:
        card("Faturamento", "R$ 32.500")
    with col4:
        card("Em produção hoje", "12")

    st.markdown("### 📈 Faturamento Mensal")

    st.line_chart({
        "2025": [12000, 15000, 17500, 20000, 22000, 25000]
    })

    st.markdown("### ⭐ Top 5 produtos mais vendidos")
    st.bar_chart({
        "vendas": [80, 65, 60, 45, 40]
    })

    st.markdown("### 📝 Últimos pedidos")
    st.dataframe({
        "Pedido": [101, 102, 103],
        "Cliente": ["Maria", "João", "Carlos"],
        "Status": ["Em produção", "Enviado", "Aguardando pagamento"]
    })
