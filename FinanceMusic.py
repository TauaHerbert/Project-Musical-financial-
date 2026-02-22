import streamlit as stml

class finance_music():
    @staticmethod
    def inicial_memory():
        if "transport_socio1" not in stml.session_state:
            stml.session_state.transport_socio1 = [0.0]
        if "transport_socio2" not in stml.session_state:
            stml.session_state.transport_socio2 = [0.0]
        if "music_contrat" not in stml.session_state:
            stml.session_state.music_contrat = [{"nome": "", "valor": 0.0}]
        if "outros_gastos" not in stml.session_state:
            stml.session_state.outros_gastos = [{"descricao": "", "valor": 0.0}]

    @staticmethod
    def adicionar_campo(lista_nome):
        stml.session_state[lista_nome].append(0.0)

    @staticmethod
    def adicionar_musico():
        stml.session_state.music_contrat.append({"nome": "", "valor": 0.0})

    @staticmethod
    def adicionar_gastos():
        stml.session_state.outros_gastos.append({"descricao": "", "valor": 0.0})

    @staticmethod
    def remover_campo(lista_nome, indice):
        if len(stml.session_state[lista_nome]) > 1:
            stml.session_state[lista_nome].pop(indice)
        else:
            if lista_nome == "music_contrat":
                stml.session_state[lista_nome] = [{"nome": "", "valor": 0.0}]
            elif lista_nome == "outros_gastos":
                stml.session_state[lista_nome] = [{"descricao": "", "valor": 0.0}]
            else:
                stml.session_state[lista_nome] = [0.0]

    @staticmethod
    def gerar_relatorio(cache_total, cache_agenciador, total_transport, total_music_cache, total_gastos, total_socio1, total_socio2, contratante, data_evento, agenciador):

            resul = cache_total - (cache_agenciador + total_transport + total_music_cache + total_gastos)
            stml.info(f"TOTAL LIQUIDO (R$): {resul:.2f}")

            resulTD = resul / 2
            detalhe_socio1_transporte = " + ".join([str(v) for v in stml.session_state.transport_socio1])
            detalhe_socio2_transporte = " + ".join([str(v) for v in stml.session_state.transport_socio2])
            final_cache_socio1 = resulTD + total_socio1
            final_cache_socio2 = resulTD + total_socio2

            info_musicos = ""
            info_gastos = ""

            for m in stml.session_state.music_contrat:
                if m["nome"] or m["valor"]:
                    info_musicos += f"\n{m['nome'].upper()} (R$ {m['valor']:.2f})"
            if not info_musicos or info_musicos.isspace():
                info_musicos = "Nenhum músico contratado!".upper()

            for g in stml.session_state.outros_gastos:
                if g["descricao"] or g["valor"]:
                    info_gastos += f"\n{g['descricao'].upper()} (R$ {g['valor']:.2f})"
            if not info_gastos or info_gastos.isspace():
                info_gastos = "Nenhum gasto extra!".upper()

            relatorio = f"""
        *Contratante:* {contratante}
*Data:* {data_evento.strftime('%d/%m/%Y')}

*Cache:* R$ {cache_total:.2f}
- *Transporte:* Total R$ {total_transport:.2f}
     Uber Socio 1: {detalhe_socio1_transporte} R$ {total_socio1:.2f}
     Uber Socio 2: {detalhe_socio2_transporte} R$ {total_socio2:.2f}

- *Agenciador(a):* {agenciador} (R$ {cache_agenciador:.2f})
- *Contratados(a):* {info_musicos}
- *Outros Gastos:* {info_gastos}

Total: R$ {resul} / 2 = *{resulTD:.2f}*

*Socio 1* {total_socio1:.2f} + {resulTD:.2f} = *R$ {final_cache_socio1:.2f}*
*Socio 2* {total_socio2:.2f} + {resulTD:.2f} = *R$ {final_cache_socio2:.2f}*
{info_musicos}"""

            stml.divider()
            stml.subheader("📋 Relatório para WhatsApp")
            stml.code(relatorio, language="text")