import streamlit as st

def inject_css():
    st.markdown("""
        <style>

        /* Fonte */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
        }

        /* Sidebar */
        section[data-testid='stSidebar'] {
            background-color: #111827 !important;
        }
        .css-1d391kg { background-color: #111827 !important; }

        /* Sidebar titles */
        .sidebar-title {
            color: #fff;
            font-size: 1.3rem;
            font-weight: 600;
            padding: 15px 10px 5px 10px;
        }

        /* Cards */
        .card {
            background: #ffffff;
            padding: 18px 20px;
            border-radius: 14px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.06);
            border: 1px solid #f1f1f1;
        }
        .card h3 {
            margin: 0;
            font-size: 1.1rem;
            color: #374151;
            font-weight: 600;
        }
        .card .value {
            font-size: 1.7rem;
            font-weight: 700;
            margin-top: 10px;
            color: #111827;
        }

        /* Tabelas */
        .stDataFrame table {
            border-radius: 10px !important;
            overflow: hidden;
        }

        /* Header */
        .page-title {
            font-size: 2rem;
            font-weight: 700;
            color: #111827;
            margin-bottom: 8px;
        }

        .page-subtitle {
            font-size: 1rem;
            color: #6B7280;
            margin-bottom: 25px;
        }

        /* Botões */
        .stButton>button {
            background: linear-gradient(90deg, #2563EB, #3B82F6);
            color: #fff;
            border: none;
            padding: 9px 20px;
            border-radius: 8px;
            font-weight: 600;
        }
        .stButton>button:hover {
            opacity: .92;
        }

        /* Campos */
        input, select, textarea {
            border-radius: 8px !important;
        }

        </style>
    """, unsafe_allow_html=True)


def header(title, subtitle=None):
    st.markdown(f"<div class='page-title'>{title}</div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div class='page-subtitle'>{subtitle}</div>", unsafe_allow_html=True)


def card(title, value):
    st.markdown(
        f"""
        <div class='card'>
            <h3>{title}</h3>
            <div class='value'>{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
