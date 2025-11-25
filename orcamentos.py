import streamlit as st
from ui import inject_css, header

def orcamentos():
    inject_css()
    header("Orçamentos", "Crie e gerencie orçamentos")

    cliente = st.selectbox("Cliente", ["Maria", "João", "Carlos"])
    st.markdown("### Itens")

    with st.expander("Adicionar item"):
        produto = st.selectbox("Produto", ["Adesivo", "Banner", "Placa PVC"])
        tipo = st.selectbox("Tipo", ["un", "m2"])
        quantidade = st.number_input("Quantidade", 1)
        largura = st.number_input("Largura (cm)", 0)
        altura = st.number_input("Altura (cm)", 0)
        valor_unit = st.number_input("Valor unitário", 0.0)

        if tipo == "un":
            total = quantidade * valor_unit
        else:
            area = (largura/100)*(altura/100)
            total = area * quantidade * valor_unit

        st.info(f"Total do item: **R$ {total:.2f}**")

        st.button("Adicionar item")

    st.markdown("### Resumo")
    st.write("Valor total: R$ 0,00")

    st.button("Gerar PDF / Enviar pelo WhatsApp")
