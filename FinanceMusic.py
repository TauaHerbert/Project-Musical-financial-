import streamlit as stml

class finance_music():
    @staticmethod
    def inicial_memory():
        """
            Inicializa o estado da sessão (session_state) para os dados do gerenciamento financeiro.

            Este método atua como um 'banco de dados têmmporario' da aplicação, garantindo que as estruturas
            de dados necessárias para armazenar gastos de transporte, músicos contratados
            e outras despesas estejam disponíveis na memória do Streamlit antes da
            renderização dos componentes.

            As chaves são inicializadas apenas se não existirem, evitando a perda de dados
            durante o ciclo de vida da aplicação.
        """
        # Verifica e inicializa transporte para o sócio 1
        if "transport_socio1" not in stml.session_state:
            stml.session_state.transport_socio1 = [0.0]
        # Verifica e inicializa transporte para o sócio 2
        if "transport_socio2" not in stml.session_state:
            stml.session_state.transport_socio2 = [0.0]
        # Inicializa estrutura para músicos (Nome e Valor do cachê)
        if "music_contrat" not in stml.session_state:
            stml.session_state.music_contrat = [{"nome": "", "valor": 0.0}]
        # Inicializa estrutura para gastos diversos (Descrição e Valor)
        if "outros_gastos" not in stml.session_state:
            stml.session_state.outros_gastos = [{"descricao": "", "valor": 0.0}]

    @staticmethod
    def adicionar_campo(lista_nome):
        """
            Adiciona uma nova linha para inserir o valor de corrida tanto do socio1 quanto do socio2.

            Esse metodo serve para acrescentar mais uma corrida para ambos os socios,
            permitindo adicionar vários gastos de transporte depois (usando o append).
        """
        stml.session_state[lista_nome].append(0.0)

    @staticmethod
    def adicionar_musico():
        """
            Adiciona uma nova linha para inserir informações de músicos contratados.

            Esse metodo serve para acrescentar mais músicos de acordo com a nescessidade,
            permitindo adicionar vários músicos (usando o append).
        """
        stml.session_state.music_contrat.append({"nome": "", "valor": 0.0})

    @staticmethod
    def adicionar_gastos():
        """
            Adiciona uma nova linha para inserir informações de gastos.

            Esse metodo serve para acrescentar mais gastos de acordo com a nescessidade,
            permitindo adicionar vários gastos (usando o append).
        """
        stml.session_state.outros_gastos.append({"descricao": "", "valor": 0.0})

    @staticmethod
    def remover_campo(lista_nome, indice):
        """
            Remove um item específico de uma lista no session_state ou reseta o campo se for o último.

            Este método garante que a interface do Streamlit nunca fique sem ao menos um campo
            visível, reinicializando o dicionário com valores padrão caso o usuário tente
            remover o único item restante.

        """
        if len(stml.session_state[lista_nome]) > 1:
            # Remove o elemento pelo índice se houver mais de um na lista
            stml.session_state[lista_nome].pop(indice)
        else:
            # Lógica de "Reset": Se for o último item, limpa os valores em vez de deletar a lista
            if lista_nome == "music_contrat":
                stml.session_state[lista_nome] = [{"nome": "", "valor": 0.0}]
            elif lista_nome == "outros_gastos":
                stml.session_state[lista_nome] = [{"descricao": "", "valor": 0.0}]
            else:
                stml.session_state[lista_nome] = [0.0]

    @staticmethod
    def gerar_relatorio(cache_total, cache_agenciador, total_transport, total_music_cache, total_gastos, total_socio1, total_socio2, contratante, data_evento, agenciador):
            """
                Método principal da aplicação, serve para gerar o relatório final com base em todas a informações
                cadastradas.

                Este método recebe todas as informações adicionadas no cadastro para elaborar os calculos
                e gerar um relatorio com as informações principais:

                - Gastos individuas dos sócios (corridas)
                - Gasto total do transporte
                - Calculo para o pagamento do valor líquido dos sócios
                - Calculo total dos vlores dos músicos contratados
                - calculo total de gastos

                O relatorio alem dos informações principais exibe tambems informações importantes do cadastro como:

                - Contratante
                - Data do evento (show)
                - Cachê total
                - Agenciador e seu Cachê

                O método gera uma mensagem de texto com caracters especificos para whatsapp, podendo copiar
                diretamente do conteiner.
            """

            # Calculo para gerar o valor liquido a ser dividido entre os sócios.
            resul = cache_total - (cache_agenciador + total_transport + total_music_cache + total_gastos)
            stml.info(f"TOTAL LIQUIDO (R$): {resul:.2f}")

            # Dívisão do valor liquido para os sóscios
            resulTD = resul / 2
            # Detalhe das corridas índividuais de cada sócio
            detalhe_socio1_transporte = " + ".join([str(v) for v in stml.session_state.transport_socio1])
            detalhe_socio2_transporte = " + ".join([str(v) for v in stml.session_state.transport_socio2])
            # Valor total a receber dos socios (valor liquido índividual + valor tota das corridas índividuais)
            final_cache_socio1 = resulTD + total_socio1
            final_cache_socio2 = resulTD + total_socio2

            # Inicialização da variaveis de informações dos músicos contratados e gastos.
            info_musicos = ""
            info_gastos = ""

            # Lógica para alimentar a variavel info_musicos.
            for m in stml.session_state.music_contrat:
                # Caso encontre algum musico na memôria (session_state.music_contrat) a variavel é preenchida.
                if m["nome"] or m["valor"]:
                    info_musicos += f"\n{m['nome'].upper()} (R$ {m['valor']:.2f})"
            # Caso não encontre nenhum musico a variavel recebe um texto informando.
            if not info_musicos or info_musicos.isspace():
                info_musicos = "Nenhum músico contratado!".upper()

            # Lógica para alimentar a variavel info_gastos.
            for g in stml.session_state.outros_gastos:
                # Caso encontre algum gasto na memôria (session_state.outros_gastos) a variavel é preenchida.
                if g["descricao"] or g["valor"]:
                    info_gastos += f"\n{g['descricao'].upper()} (R$ {g['valor']:.2f})"
            # Caso não encontre nenhum gasto a variavel recebe um texto informando.
            if not info_gastos or info_gastos.isspace():
                info_gastos = "Nenhum gasto extra!".upper()

        # Elaboração e construção do relatório com base na informações calculadas e dados recebidos pelo método.
            relatorio = f"""
        Contratante: *{contratante}*
Data: {data_evento.strftime('%d/%m/%Y')}

Cache: R$ *{cache_total:.2f}*
- Transporte: *Total R$ {total_transport:.2f}*
     Uber: {detalhe_socio1_transporte} *Socio 1 R$ {total_socio1:.2f}*
     Uber: {detalhe_socio2_transporte} *Socio 2 R$ {total_socio2:.2f}*

- Agenciador(a): {agenciador} (R$ {cache_agenciador:.2f})
- Contratados(a): {info_musicos}
- Outros Gastos: {info_gastos}

Total: R$ {resul} ÷ 2 = *R$ {resulTD:.2f}*

*Socio 1* {total_socio1:.2f} + {resulTD:.2f} = *R$ {final_cache_socio1:.2f}*
*Socio 2* {total_socio2:.2f} + {resulTD:.2f} = *R$ {final_cache_socio2:.2f}*
{info_musicos}"""

            stml.divider()
            stml.subheader("📋 Relatório para WhatsApp")
            # Opção para copiar o texto (Relatório).
            stml.code(relatorio, language="text")