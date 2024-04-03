import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Histórico",
    page_icon="⏳"
)

st.title("Histórico")

tab1, tab2, tab3 = st.tabs(["2020", "2021", "2022"])

with tab1:
    dados2020 = pd.read_excel('data/dados_2020.xlsx')
    tab1colmet1, tab1colmet2, tab1colmet3 = st.columns(3)

    tab1colmet1.metric(
        label = "Bolsistas",
        value = dados2020[dados2020['bolsista_2020']==1]['bolsista_2020'].count()
    )

    tab1colmet2.metric(
        label = "Ponto de virada",
        value = dados2020[dados2020['ponto_virada_2020']==1]['ponto_virada_2020'].count()
    )

    tab1colmet3.metric(
        label = 'INDE > 8',
        value = dados2020[dados2020['inde_2020']>8]['inde_2020'].count()
    )
    
    dados_qtd_unidades = dados2020.copy()
    dados_qtd_unidades = dados_qtd_unidades.groupby(['unidades'])['nome'].count().reset_index()

    graf_qtd_unidades = px.bar(dados_qtd_unidades,
                           x='unidades',
                           y='nome',
                           title='Quantidade de alunos por unidade',
                           labels={
                               'unidades': 'Unidade',
                               'nome': 'Quantidade'
                           },
                           hover_name='unidades',
                           color = 'unidades',
                           color_discrete_sequence=[px.colors.qualitative.Pastel[0],
                                                    px.colors.qualitative.Pastel[1],
                                                    px.colors.qualitative.Pastel[2],
                                                    px.colors.qualitative.Pastel[9],
                                                    px.colors.qualitative.Pastel[8]])
    
    graf_qtd_unidades.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_qtd_unidades, use_container_width=True)

    dados_bolsistas_unidades = dados2020.copy()
    dados_bolsistas_unidades = dados_bolsistas_unidades[dados_bolsistas_unidades['bolsista_2020']==1]
    dados_bolsistas_unidades = dados_bolsistas_unidades.groupby(['unidades'])['nome'].count().reset_index()

    graf_bolsistas_unidades = px.bar(dados_bolsistas_unidades,
                        x='unidades',
                        y='nome',
                        title='Quantidade de bolsistas por unidade',
                        labels={
                            'unidades': 'Unidade',
                            'nome': 'Quantidade'
                        },
                        hover_name='unidades',
                        color = 'unidades',
                        color_discrete_sequence=[px.colors.qualitative.Pastel[0],
                                                px.colors.qualitative.Pastel[1],
                                                px.colors.qualitative.Pastel[2],
                                                px.colors.qualitative.Pastel[8]])
    
    graf_bolsistas_unidades.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_bolsistas_unidades, use_container_width=True)

    dados_indices_unidades = dados2020.copy()
    dados_indices_unidades.drop(['bolsista_2020', 'anos_pm_2020', 'ponto_virada_2020', 'pedra_2020', 'fase', 'turma'], axis = 1, inplace = True)

    filtro_indice = st.multiselect("Selecione os índices de desenvolvimento que deseja visualizar", ['inde_2020', 'iaa_2020', 'ieg_2020', 'ips_2020', 'ida_2020', 'ipp_2020', 'ipv_2020', 'ian_2020'], ['inde_2020', 'iaa_2020', 'ieg_2020', 'ips_2020', 'ida_2020', 'ipp_2020', 'ipv_2020', 'ian_2020'])

    dados_indices_unidades = dados_indices_unidades.groupby(['unidades'])[filtro_indice].mean().reset_index()
    dados_indices_unidades.set_index(dados_indices_unidades['unidades'], inplace=True)
    dados_indices_unidades.drop('unidades', axis = 1, inplace = True)

    if filtro_indice:
        # Plotar o gráfico de barras múltiplas com base nas colunas selecionadas
        fig, ax = plt.subplots()
        dados_indices_unidades.plot(kind='bar', ax=ax)
        plt.xlabel('Unidades')
        plt.ylabel('Valores')
        plt.title('Média dos índices de avaliação por unidade')
        plt.xticks(rotation=360)
        plt.ylim(0, 9)
        sns.set_style("darkgrid", {"grid.color": ".6", 'grid.linestyle': '-.'})
        sns.color_palette("Blues")
        plt.legend(loc = 'upper right', bbox_to_anchor = (1.3, 1), shadow = True, facecolor = 'white')
        st.pyplot(fig)

        st.table(dados_indices_unidades)
    else:
        st.write("Por favor, selecione pelo menos uma coluna.")

    dados_qtd_fases = dados2020.copy()
    dados_qtd_fases = dados_qtd_fases.groupby(['fase'])['nome'].count().reset_index()

    graf_qtd_fases = px.bar(dados_qtd_fases,
                            x='fase',
                            y='nome',
                            title='Quantidade de alunos por fase',
                            labels={
                                'fase': 'Fase',
                                'nome': 'Quantidade'
                            },
                            color = 'fase',
                            color_continuous_scale=px.colors.sequential.Aggrnyl_r)
    
    graf_qtd_fases.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_qtd_fases, use_container_width=True)


    dados_inde_fases = dados2020.copy()
    dados_inde_fases = dados_inde_fases.groupby(['fase'])['inde_2020'].mean().reset_index()

    graf_inde_fases = px.bar(dados_inde_fases,
                            x='fase',
                            y='inde_2020',
                            title='Média do INDE por fase',
                            labels={
                                'fase': 'Fase',
                                'inde_2020': 'INDE'
                            },
                            color = 'fase',
                            color_continuous_scale=px.colors.sequential.Aggrnyl_r)

    graf_inde_fases.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_inde_fases, use_container_width=True)

with tab2:
    dados2021 = pd.read_excel('data/dados_2021.xlsx')
    tab2colmet1, tab2colmet2, tab2colmet3 = st.columns(3)

    tab2colmet1.metric(
        label = "Bolsistas",
        value = dados2021[dados2021['bolsista_2021']==1]['bolsista_2021'].count()
    )

    tab2colmet2.metric(
        label = "Ponto de virada",
        value = dados2021[dados2021['ponto_virada_2021']==1]['ponto_virada_2021'].count()
    )

    tab2colmet3.metric(
        label = 'INDE > 8',
        value = dados2021[dados2021['inde_2021']>8]['inde_2021'].count()
    )
    
    dados_qtd_unidades = dados2021.copy()
    dados_qtd_unidades = dados_qtd_unidades.groupby(['unidades'])['nome'].count().reset_index()

    graf_qtd_unidades = px.bar(dados_qtd_unidades,
                           x='unidades',
                           y='nome',
                           title='Quantidade de alunos por unidade',
                           labels={
                               'unidades': 'Unidade',
                               'nome': 'Quantidade'
                           },
                           hover_name='unidades',
                           color = 'unidades',
                           color_discrete_sequence=[px.colors.qualitative.Pastel[0],
                                                    px.colors.qualitative.Pastel[1],
                                                    px.colors.qualitative.Pastel[2],
                                                    px.colors.qualitative.Pastel[9],
                                                    px.colors.qualitative.Pastel[8]])
    
    graf_qtd_unidades.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_qtd_unidades, use_container_width=True)

    dados_bolsistas_unidades = dados2021.copy()
    dados_bolsistas_unidades = dados_bolsistas_unidades[dados_bolsistas_unidades['bolsista_2021']==1]
    dados_bolsistas_unidades = dados_bolsistas_unidades.groupby(['unidades'])['nome'].count().reset_index()

    graf_bolsistas_unidades = px.bar(dados_bolsistas_unidades,
                        x='unidades',
                        y='nome',
                        title='Quantidade de bolsistas por unidade',
                        labels={
                            'unidades': 'Unidade',
                            'nome': 'Quantidade'
                        },
                        hover_name='unidades',
                        color = 'unidades',
                        color_discrete_sequence=[px.colors.qualitative.Pastel[0],
                                                px.colors.qualitative.Pastel[1],
                                                px.colors.qualitative.Pastel[2],
                                                px.colors.qualitative.Pastel[8]])
    
    graf_bolsistas_unidades.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_bolsistas_unidades, use_container_width=True)

    dados_indices_unidades = dados2021.copy()
    dados_indices_unidades.drop(['bolsista_2021', 'anos_pm_2021', 'ponto_virada_2021', 'pedra_2021', 'fase', 'turma'], axis = 1, inplace = True)

    filtro_indice = st.multiselect("Selecione os índices de desenvolvimento que deseja visualizar", ['inde_2021', 'iaa_2021', 'ieg_2021', 'ips_2021', 'ida_2021', 'ipp_2021', 'ipv_2021', 'ian_2021'], ['inde_2021', 'iaa_2021', 'ieg_2021', 'ips_2021', 'ida_2021', 'ipp_2021', 'ipv_2021', 'ian_2021'])

    dados_indices_unidades = dados_indices_unidades.groupby(['unidades'])[filtro_indice].mean().reset_index()
    dados_indices_unidades.set_index(dados_indices_unidades['unidades'], inplace=True)
    dados_indices_unidades.drop('unidades', axis = 1, inplace = True)

    if filtro_indice:
        # Plotar o gráfico de barras múltiplas com base nas colunas selecionadas
        fig, ax = plt.subplots()
        dados_indices_unidades.plot(kind='bar', ax=ax)
        plt.xlabel('Unidades')
        plt.ylabel('Valores')
        plt.title('Média dos índices de avaliação por unidade')
        plt.xticks(rotation=360)
        plt.ylim(0, 9)
        sns.set_style("darkgrid", {"grid.color": ".6", 'grid.linestyle': '-.'})
        sns.color_palette("Blues")
        plt.legend(loc = 'upper right', bbox_to_anchor = (1.3, 1), shadow = True, facecolor = 'white')
        st.pyplot(fig)

        st.table(dados_indices_unidades)
    else:
        st.write("Por favor, selecione pelo menos uma coluna.")

    dados_qtd_fases = dados2021.copy()
    dados_qtd_fases = dados_qtd_fases.groupby(['fase'])['nome'].count().reset_index()

    graf_qtd_fases = px.bar(dados_qtd_fases,
                            x='fase',
                            y='nome',
                            title='Quantidade de alunos por fase',
                            labels={
                                'fase': 'Fase',
                                'nome': 'Quantidade'
                            },
                            color = 'fase',
                            color_continuous_scale=px.colors.sequential.Aggrnyl_r)
    
    graf_qtd_fases.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_qtd_fases, use_container_width=True)


    dados_inde_fases = dados2021.copy()
    dados_inde_fases = dados_inde_fases.groupby(['fase'])['inde_2021'].mean().reset_index()

    graf_inde_fases = px.bar(dados_inde_fases,
                            x='fase',
                            y='inde_2021',
                            title='Média do INDE por fase',
                            labels={
                                'fase': 'Fase',
                                'inde_2021': 'INDE'
                            },
                            color = 'fase',
                            color_continuous_scale=px.colors.sequential.Aggrnyl_r)
    
    graf_inde_fases.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_inde_fases, use_container_width=True)

with tab3:
    dados2022 = pd.read_excel('data/dados_2022.xlsx')
    tab2colmet1, tab2colmet2, tab2colmet3 = st.columns(3)

    tab2colmet1.metric(
        label = "Bolsistas",
        value = dados2022[dados2022['bolsista_2022']==1]['bolsista_2022'].count()
    )

    tab2colmet2.metric(
        label = "Ponto de virada",
        value = dados2022[dados2022['ponto_virada_2022']==1]['ponto_virada_2022'].count()
    )

    tab2colmet3.metric(
        label = 'INDE > 8',
        value = dados2022[dados2022['inde_2022']>8]['inde_2022'].count()
    )
    
    dados_qtd_unidades = dados2022.copy()
    dados_qtd_unidades = dados_qtd_unidades.groupby(['unidades'])['nome'].count().reset_index()

    graf_qtd_unidades = px.bar(dados_qtd_unidades,
                           x='unidades',
                           y='nome',
                           title='Quantidade de alunos por unidade',
                           labels={
                               'unidades': 'Unidade',
                               'nome': 'Quantidade'
                           },
                           hover_name='unidades',
                           color = 'unidades',
                           color_discrete_sequence=[px.colors.qualitative.Pastel[0],
                                                    px.colors.qualitative.Pastel[1],
                                                    px.colors.qualitative.Pastel[2],
                                                    px.colors.qualitative.Pastel[9],
                                                    px.colors.qualitative.Pastel[8]])
    
    graf_qtd_unidades.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_qtd_unidades, use_container_width=True)

    dados_bolsistas_unidades = dados2022.copy()
    dados_bolsistas_unidades = dados_bolsistas_unidades[dados_bolsistas_unidades['bolsista_2022']==1]
    dados_bolsistas_unidades = dados_bolsistas_unidades.groupby(['unidades'])['nome'].count().reset_index()

    graf_bolsistas_unidades = px.bar(dados_bolsistas_unidades,
                        x='unidades',
                        y='nome',
                        title='Quantidade de bolsistas por unidade',
                        labels={
                            'unidades': 'Unidade',
                            'nome': 'Quantidade'
                        },
                        hover_name='unidades',
                        color = 'unidades',
                        color_discrete_sequence=[px.colors.qualitative.Pastel[0],
                                                px.colors.qualitative.Pastel[1],
                                                px.colors.qualitative.Pastel[2],
                                                px.colors.qualitative.Pastel[8]])
    
    graf_bolsistas_unidades.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_bolsistas_unidades, use_container_width=True)

    dados_indices_unidades = dados2022.copy()
    dados_indices_unidades.drop(['bolsista_2022', 'anos_pm_2022', 'ponto_virada_2022', 'pedra_2022', 'fase', 'turma'], axis = 1, inplace = True)

    filtro_indice = st.multiselect("Selecione os índices de desenvolvimento que deseja visualizar", ['inde_2022', 'iaa_2022', 'ieg_2022', 'ips_2022', 'ida_2022', 'ipp_2022', 'ipv_2022', 'ian_2022'], ['inde_2022', 'iaa_2022', 'ieg_2022', 'ips_2022', 'ida_2022', 'ipp_2022', 'ipv_2022', 'ian_2022'])

    dados_indices_unidades = dados_indices_unidades.groupby(['unidades'])[filtro_indice].mean().reset_index()
    dados_indices_unidades.set_index(dados_indices_unidades['unidades'], inplace=True)
    dados_indices_unidades.drop('unidades', axis = 1, inplace = True)

    if filtro_indice:
        # Plotar o gráfico de barras múltiplas com base nas colunas selecionadas
        fig, ax = plt.subplots()
        dados_indices_unidades.plot(kind='bar', ax=ax)
        plt.xlabel('Unidades')
        plt.ylabel('Valores')
        plt.title('Média dos índices de avaliação por unidade')
        plt.xticks(rotation=360)
        plt.ylim(0, 9)
        sns.set_style("darkgrid", {"grid.color": ".6", 'grid.linestyle': '-.'})
        sns.color_palette("Blues")
        plt.legend(loc = 'upper right', bbox_to_anchor = (1.3, 1), shadow = True, facecolor = 'white')
        st.pyplot(fig)

        st.table(dados_indices_unidades)
    else:
        st.write("Por favor, selecione pelo menos uma coluna.")

    dados_qtd_fases = dados2022.copy()
    dados_qtd_fases = dados_qtd_fases.groupby(['fase'])['nome'].count().reset_index()

    graf_qtd_fases = px.bar(dados_qtd_fases,
                            x='fase',
                            y='nome',
                            title='Quantidade de alunos por fase',
                            labels={
                                'fase': 'Fase',
                                'nome': 'Quantidade'
                            },
                            color = 'fase',
                            color_continuous_scale=px.colors.sequential.Aggrnyl_r)
    
    graf_qtd_fases.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_qtd_fases, use_container_width=True)


    dados_inde_fases = dados2022.copy()
    dados_inde_fases = dados_inde_fases.groupby(['fase'])['inde_2022'].mean().reset_index()

    graf_inde_fases = px.bar(dados_inde_fases,
                            x='fase',
                            y='inde_2022',
                            title='Média do INDE por fase',
                            labels={
                                'fase': 'Fase',
                                'inde_2022': 'INDE'
                            },
                            color = 'fase',
                            color_continuous_scale=px.colors.sequential.Aggrnyl_r)
    
    graf_inde_fases.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=23 
    )

    st.plotly_chart(graf_inde_fases, use_container_width=True)