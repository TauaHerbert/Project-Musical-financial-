import streamlit as stml
from datetime import date
from FinanceMusic import finance_music as fm

stml.markdown("""
    <style>
        </style>"""
              ,unsafe_allow_html=True)

stml.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #121212 0%, #0f2027 100%);
        background-attachment: fixed;
    }
    
    .stWidgetLabel p, label, .st-at, .st-ae {
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
        text-shadow: 1px 1px 2px black !important;
    }

    .stTextInput input, .stNumberInput input, .stDateInput input {
        color: #000000 !important;
        background-color: #e1e5eb !important;
        font-weight: 400 !important;
        border: 1px solid #1E90FF !important;
    }

    .stMarkdown p, .stText p {
        color: white !important;
    }

    [data-testid="stVerticalBlock"] {
        background-color: rgba(255, 255, 255, 0.02);
        padding: 10px;
        border-radius: 10px;
    }
    
    div[data-baseweb="calendar"] button, div[data-baseweb="calendar"] div {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

stml.markdown("""
    <div style='color: white; padding: 10px; text-align: center; font-family: sans-serif; 
                font-weight: bold; font-size: 40px; margin-bottom: 50px; background-color: rgba(0,0,0,0.5); 
                text-shadow: 2px 2px 4px #1E90FF;
        box-shadow: 0px 4px 10px #1E90FF;'>
        🎼 Financeiro Musical 🎼 
    </div>
""", unsafe_allow_html=True)

fm.inicial_memory()

with stml.container():

    col_contratante, col_cache_contrat, col_data = stml.columns(3)
    with col_contratante:
        contratante = stml.text_input("CONTRATANTE: ").upper()
    with col_cache_contrat:
        cache_total = stml.number_input("VALOR DO CACHÊ (R$):", min_value=0.0, step=50.0)
    with col_data:
        data_evento = stml.date_input("DATA DO SHOW:", date.today())

    col_agenciador, col_cache_agenciador = stml.columns(2)

    with col_agenciador:
        agenciador = stml.text_input("AGENCIADOR(A): ")
    with col_cache_agenciador:
        cache_agenciador = stml.number_input("TAXA DO AGENCIADOR (R$): ", min_value=0.0, step=50.0)

stml.divider()

stml.markdown("""
    <div style='background-color: #000000; color: white; padding: 10px; 
                border-radius: 8px; text-align: center; font-family: sans-serif; 
                font-weight: bold; font-size: 24px; margin-bottom: 45px; text-shadow: 2px 2px 4px #1E90FF; 
                box-shadow: 0px 4px 10px #1E90FF;'>
        🚚 TRANSPORTE
    </div>
""", unsafe_allow_html=True)
stml.write("**TRANSPORTE Socio 1**")

for i, valor in enumerate(stml.session_state.transport_socio1):
    col_input, col_lixeira = stml.columns([4, 0.5])

    with col_input:
        stml.session_state.transport_socio1[i] = stml.number_input(
            f"CORRIDA {i + 1} (R$)",
            value=valor,
            key=f"socio1_input_{i}",
            min_value=0.0, step=10.0
        )

    with col_lixeira:
        #stml.markdown("<p style='margin-bottom: 7px; font-size: 12px; font-weight: bold;'>EXCLUIR</p>", unsafe_allow_html=True)
        stml.write(" ")
        stml.write(" ")
        stml.button("🗑️", key=f"socio1_del_{i}", on_click=fm.remover_campo, args=("transport_socio1", i), help="Apagar corrida")

stml.button("➕ Adicionar Corrida (Socio 1)", on_click=fm.adicionar_campo, args=("transport_socio1",))

stml.write("**TRANSPORTE Socio 2**")

for i, valor in enumerate(stml.session_state.transport_socio2):
    col_input, col_lixeira = stml.columns([4, 0.5])

    with col_input:
        stml.session_state.transport_socio2[i] = stml.number_input(
            f"CORRIDA {i + 1} (R$)",
            value=valor,
            key=f"socio2_input_{i}",
            min_value=0.0, step=10.0
        )

    with col_lixeira:
        #stml.markdown("<p style='margin-bottom: 7px; font-size: 12px; font-weight: bold;'>EXCLUIR</p>", unsafe_allow_html=True)
        stml.write(" ")
        stml.write(" ")
        stml.button("🗑️", key=f"socio2_del_{i}", on_click=fm.remover_campo, args=("transport_socio2", i), help="Apagar corrida")

stml.button("➕ Adicionar Corrida (Socio 2)", on_click=fm.adicionar_campo, args=("transport_socio2",))

total_socio1 = sum(stml.session_state.transport_socio1)
total_socio2 = sum(stml.session_state.transport_socio2)
total_transport = total_socio1 + total_socio2
stml.info(f"Socio 1: R$ {total_socio1:.2f} | Socio 2: R$ {total_socio2:.2f}  |  TOTAL TRANSPORT: R$ {total_transport:.2f}")

stml.divider()

stml.markdown("""
    <div style='background-color: #000000; color: white; padding: 10px; 
                border-radius: 8px; text-align: center; font-family: sans-serif; 
                font-weight: bold; font-size: 24px; margin-bottom: 45px; text-shadow: 2px 2px 4px #1E90FF; 
                box-shadow: 0px 4px 10px #1E90FF;'>
        🎸 MÚSICOS CONTRATADOS
    </div>
""", unsafe_allow_html=True)

for i, musico in enumerate(stml.session_state.music_contrat):
    col_nome, col_valor, col_lixeira = stml.columns([2.5, 1.5, 0.5])

    with col_nome:
        stml.session_state.music_contrat[i]["nome"] = stml.text_input(
            f"Nome do Músico {i + 1}",
            value=musico["nome"],
            key=f"music_nome_{i}"
        )
    with col_valor:
        stml.session_state.music_contrat[i]["valor"] = stml.number_input(
            f"Cachê (R$)",
            value=musico["valor"],
            key=f"music_val_{i}",
            min_value=0.0, step=50.0
        )
    with col_lixeira:
        stml.write(" ")
        stml.write(" ")
        stml.button("🗑️", key=f"music_contrat_del_{i}", on_click=fm.remover_campo, args=("music_contrat", i), help="Apagar musico")

stml.button("➕ Adicionar um novo Musico", on_click=fm.adicionar_musico)

total_music_cache = sum(m["valor"] for m in stml.session_state.music_contrat)

stml.info(f"TOTAL (R$): {total_music_cache}")

stml.divider()

stml.markdown("""
    <div style='background-color: #000000; color: white; padding: 10px; 
                border-radius: 8px; text-align: center; font-family: sans-serif; 
                font-weight: bold; font-size: 24px; margin-bottom: 45px; text-shadow: 2px 2px 4px #1E90FF; 
                box-shadow: 0px 4px 10px #1E90FF;'>
        💸 OUTROS GASTOS
    </div>
""", unsafe_allow_html=True)

for i, gastos in enumerate(stml.session_state.outros_gastos):
    col_nome, col_valor, col_lixeira = stml.columns([2.5, 1.5, 0.5])


    with col_nome:
        stml.session_state.outros_gastos[i]["descricao"] = stml.text_input(
            f"Descrição {i + 1}",
            value=gastos["descricao"],
            key=f"gastos_descricao_{i}"
        )
    with col_valor:
        stml.session_state.outros_gastos[i]["valor"] = stml.number_input(
            f"Valor (R$)",
            value=gastos["valor"],
            key=f"gastos_val_{i}",
            min_value=0.0, step=10.0
        )
    with col_lixeira:
        stml.write(" ")
        stml.write(" ")
        stml.button("🗑️", key=f"outros_gastos_del_{i}", on_click=fm.remover_campo, args=("outros_gastos", i), help="Apagar gasto")

stml.button("➕ Adicionar um novo Gasto", on_click=fm.adicionar_gastos)

total_gastos = sum(m["valor"] for m in stml.session_state.outros_gastos)

stml.info(f"TOTAL (R$): {total_gastos}")


col1, col2, col3 = stml.columns([1, 6, 1])
with col2:
    if stml.button("🎼 GERAR RELATÓRIO FINAL", type="primary", use_container_width=True):
        fm.gerar_relatorio(cache_total, cache_agenciador, total_transport,
                       total_music_cache, total_gastos, total_socio1,
                       total_socio2, contratante, data_evento, agenciador)