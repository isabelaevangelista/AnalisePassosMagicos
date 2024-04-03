import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Análises", 
    page_icon="📊")

st.title("Análises e KPIs entre 2020 e 2022")

dados = pd.read_excel('data/dados_juntos.xlsx')

alunos_anos = [['2020', dados.query('fase_2020.notna()')['fase_2020'].count()],
            ['2021', dados.query('fase_2021.notna()')['fase_2021'].count()],
            ['2022', dados.query('fase_2022.notna()')['fase_2022'].count()]]

unidades_anos = [['Centro', dados[dados['unidade_2020']=='Centro']['nome'].count(),
                                dados[dados['unidade_2021']=='Centro']['nome'].count(),
                                dados[dados['unidade_2022']=='Centro']['nome'].count()],
                 ['Filipinho', dados[dados['unidade_2020']=='Filipinho']['nome'].count(),
                                dados[dados['unidade_2021']=='Filipinho']['nome'].count(),
                                dados[dados['unidade_2022']=='Filipinho']['nome'].count()],
                 ['Cipó', dados[dados['unidade_2020']=='Cipó']['nome'].count(),
                                dados[dados['unidade_2021']=='Cipó']['nome'].count(),
                                dados[dados['unidade_2022']=='Cipó']['nome'].count()],
                 ['Granjinha', dados[dados['unidade_2020']=='Granjinha']['nome'].count(),
                                dados[dados['unidade_2021']=='Granjinha']['nome'].count(),
                                dados[dados['unidade_2022']=='Granjinha']['nome'].count()],
                 ['Outra', dados[dados['unidade_2020']=='Outra']['nome'].count(),
                                dados[dados['unidade_2021']=='Outra']['nome'].count(),
                                dados[dados['unidade_2022']=='Outra']['nome'].count()]]

qtd_alunos_anos = pd.DataFrame(alunos_anos, columns=['Ano', 'Quantidade'])
qtd_alunos_anos['Ano'] = pd.to_datetime(qtd_alunos_anos['Ano'], format='%Y')
qtd_alunos_anos['Ano'] = qtd_alunos_anos['Ano'].dt.year
qtd_alunos_anos['Quantidade'] = qtd_alunos_anos['Quantidade'].astype(int)


qtd_unidades_anos = pd.DataFrame(unidades_anos, columns=['Unidade', '2020', '2021', '2022'])
qtd_unidades_anos['2020'] = qtd_unidades_anos['2020'].astype(int)
qtd_unidades_anos['2021'] = qtd_unidades_anos['2021'].astype(int)
qtd_unidades_anos['2022'] = qtd_unidades_anos['2022'].astype(int)
qtd_unidades_anos.set_index('Unidade', inplace = True)
qtd_unidades_anos = qtd_unidades_anos.T

col1, col2 = st.columns(2)

with col1:
    graf_alunos_anos = px.bar(qtd_alunos_anos,
                              x = 'Ano',
                              y = 'Quantidade',
                              color = 'Quantidade',
                              hover_name = 'Ano',
                              title='Total de alunos',
                              color_continuous_scale=px.colors.sequential.Aggrnyl_r
                              )
    
    graf_alunos_anos.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=22
    )

    st.plotly_chart(graf_alunos_anos, use_container_width=True)

with col2:
    graf_unidades_anos = px.bar(qtd_unidades_anos,
                              x = ['2020', '2021', '2022'],
                              y = qtd_unidades_anos.columns,
                              title='Quantidade de alunos por unidade',
                              )
    
    graf_unidades_anos.update_layout(
        xaxis_title='Ano',
        yaxis_title='Quantidade',
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=22
    )

    st.plotly_chart(graf_unidades_anos, use_container_width=True)

fases_anos = [['2020', dados[dados['fase_2020'] == 0]['nome'].count(),
                       dados[dados['fase_2020'] == 1]['nome'].count(),
                       dados[dados['fase_2020'] == 2]['nome'].count(),
                       dados[dados['fase_2020'] == 3]['nome'].count(),
                       dados[dados['fase_2020'] == 4]['nome'].count(),
                       dados[dados['fase_2020'] == 5]['nome'].count(),
                       dados[dados['fase_2020'] == 6]['nome'].count(),
                       dados[dados['fase_2020'] == 7]['nome'].count(),
                       dados[dados['fase_2020'] == 8]['nome'].count()],
            ['2021', dados[dados['fase_2021'] == 0]['nome'].count(),
                       dados[dados['fase_2021'] == 1]['nome'].count(),
                       dados[dados['fase_2021'] == 2]['nome'].count(),
                       dados[dados['fase_2021'] == 3]['nome'].count(),
                       dados[dados['fase_2021'] == 4]['nome'].count(),
                       dados[dados['fase_2021'] == 5]['nome'].count(),
                       dados[dados['fase_2021'] == 6]['nome'].count(),
                       dados[dados['fase_2021'] == 7]['nome'].count(),
                       dados[dados['fase_2021'] == 8]['nome'].count()],
            ['2022', dados[dados['fase_2022'] == 0]['nome'].count(),
                       dados[dados['fase_2022'] == 1]['nome'].count(),
                       dados[dados['fase_2022'] == 2]['nome'].count(),
                       dados[dados['fase_2022'] == 3]['nome'].count(),
                       dados[dados['fase_2022'] == 4]['nome'].count(),
                       dados[dados['fase_2022'] == 5]['nome'].count(),
                       dados[dados['fase_2022'] == 6]['nome'].count(),
                       dados[dados['fase_2022'] == 7]['nome'].count(),
                       dados[dados['fase_2022'] == 8]['nome'].count()]]

qtd_fases_anos = pd.DataFrame(fases_anos, columns=['Ano', 'Fase 0', 'Fase 1', 'Fase 2', 'Fase 3', 'Fase 4', 'Fase 5', 'Fase 6', 'Fase 7', 'Fase 8'])
qtd_fases_anos['Ano'] = pd.to_datetime(qtd_fases_anos['Ano'], format='%Y')
qtd_fases_anos['Ano'] = qtd_fases_anos['Ano'].dt.year
qtd_fases_anos['Fase 0'] = qtd_fases_anos['Fase 0'].astype(int)
qtd_fases_anos['Fase 1'] = qtd_fases_anos['Fase 1'].astype(int)
qtd_fases_anos['Fase 2'] = qtd_fases_anos['Fase 2'].astype(int)
qtd_fases_anos['Fase 3'] = qtd_fases_anos['Fase 3'].astype(int)
qtd_fases_anos['Fase 4'] = qtd_fases_anos['Fase 4'].astype(int)
qtd_fases_anos['Fase 5'] = qtd_fases_anos['Fase 5'].astype(int)
qtd_fases_anos['Fase 6'] = qtd_fases_anos['Fase 6'].astype(int)
qtd_fases_anos['Fase 7'] = qtd_fases_anos['Fase 7'].astype(int)
qtd_fases_anos['Fase 8'] = qtd_fases_anos['Fase 8'].astype(int)

graf_fases_anos = px.line(qtd_fases_anos,
                          x = 'Ano',
                          y = qtd_fases_anos.columns,
                          markers = True,
                          title='Quantidade de alunos por fase',
                          )

graf_fases_anos.update_layout(
    xaxis_title='Ano',
    yaxis_title='Quantidade',
    font_family='Courier New',
    title_font_family='Roboto',
    title_font_size=22 
)

st.plotly_chart(graf_fases_anos, use_container_width=True)


pv_anos = [['2020', dados[dados['ponto_virada_2020'] == 1]['nome'].count()],
            ['2021', dados[dados['ponto_virada_2021'] == 1]['nome'].count()],
            ['2022', dados[dados['ponto_virada_2022'] == 1]['nome'].count()]]

qtd_pv_anos = pd.DataFrame(pv_anos, columns=['Ano', 'Quantidade'])
qtd_pv_anos['Ano'] = pd.to_datetime(qtd_pv_anos['Ano'], format='%Y')
qtd_pv_anos['Ano'] = qtd_pv_anos['Ano'].dt.year
qtd_pv_anos['Quantidade'] = qtd_pv_anos['Quantidade'].astype(int)

dados_pv_unidades_2020 = dados.loc[dados['ponto_virada_2020'] == 1]
dados_pv_unidades_2021 = dados.loc[dados['ponto_virada_2021'] == 1]
dados_pv_unidades_2022 = dados.loc[dados['ponto_virada_2022'] == 1]

pv_unidades_anos = [['Centro', dados_pv_unidades_2020[dados_pv_unidades_2020['unidade_2020']=='Centro']['nome'].count(),
                                dados_pv_unidades_2021[dados_pv_unidades_2021['unidade_2021']=='Centro']['nome'].count(),
                                dados_pv_unidades_2022[dados_pv_unidades_2022['unidade_2022']=='Centro']['nome'].count()],
                 ['Filipinho', dados_pv_unidades_2020[dados_pv_unidades_2020['unidade_2020']=='Filipinho']['nome'].count(),
                                dados_pv_unidades_2021[dados_pv_unidades_2021['unidade_2021']=='Filipinho']['nome'].count(),
                                dados_pv_unidades_2022[dados_pv_unidades_2022['unidade_2022']=='Filipinho']['nome'].count()],
                 ['Cipó', dados_pv_unidades_2020[dados_pv_unidades_2020['unidade_2020']=='Cipó']['nome'].count(),
                                dados_pv_unidades_2021[dados_pv_unidades_2021['unidade_2021']=='Cipó']['nome'].count(),
                                dados_pv_unidades_2022[dados_pv_unidades_2022['unidade_2022']=='Cipó']['nome'].count()],
                 ['Granjinha', dados_pv_unidades_2020[dados_pv_unidades_2020['unidade_2020']=='Granjinha']['nome'].count(),
                                dados_pv_unidades_2021[dados_pv_unidades_2021['unidade_2021']=='Granjinha']['nome'].count(),
                                dados_pv_unidades_2022[dados_pv_unidades_2022['unidade_2022']=='Granjinha']['nome'].count()],
                 ['Outra', dados_pv_unidades_2020[dados_pv_unidades_2020['unidade_2020']=='Outra']['nome'].count(),
                                dados_pv_unidades_2021[dados_pv_unidades_2021['unidade_2021']=='Outra']['nome'].count(),
                                dados_pv_unidades_2022[dados_pv_unidades_2022['unidade_2022']=='Outra']['nome'].count()]]

qtd_pv_unidades_anos = pd.DataFrame(pv_unidades_anos, columns=['Unidade', '2020', '2021', '2022'])
qtd_pv_unidades_anos['2020'] = qtd_pv_unidades_anos['2020'].astype(int)
qtd_pv_unidades_anos['2021'] = qtd_pv_unidades_anos['2021'].astype(int)
qtd_pv_unidades_anos['2022'] = qtd_pv_unidades_anos['2022'].astype(int)
qtd_pv_unidades_anos.set_index('Unidade', inplace = True)
qtd_pv_unidades_anos = qtd_pv_unidades_anos.T

col3, col4 = st.columns(2)

with col3:
    graf_pv_anos = px.bar(qtd_pv_anos,
                              x = 'Ano',
                              y = 'Quantidade',
                              color = 'Quantidade',
                              hover_name = 'Ano',
                              title='Quantidade de alunos que atingiram o<br>Ponto de Virada',
                              color_continuous_scale=px.colors.sequential.Aggrnyl_r
                              )
    
    graf_pv_anos.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=22 
    )

    st.plotly_chart(graf_pv_anos, use_container_width=True)

with col4:
    graf_pv_unidades_anos = px.bar(qtd_pv_unidades_anos,
                              x = ['2020', '2021', '2022'],
                              y = qtd_pv_unidades_anos.columns,
                              title='Quantidade de alunos que atingiram o<br>Ponto de Virada por unidade',
                              )
    
    graf_pv_unidades_anos.update_layout(
        xaxis_title='Ano',
        yaxis_title='Quantidade',
    )

    graf_pv_unidades_anos.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=22 
    )

    st.plotly_chart(graf_pv_unidades_anos, use_container_width=True)

medias_anos = [['2020', dados.query('inde_2020.notna()')['inde_2020'].mean(),
                        dados.query('iaa_2020.notna()')['iaa_2020'].mean(),
                        dados.query('ieg_2020.notna()')['ieg_2020'].mean(),
                        dados.query('ips_2020.notna()')['ips_2020'].mean(),
                        dados.query('ida_2020.notna()')['ida_2020'].mean(),
                        dados.query('ipp_2020.notna()')['ipp_2020'].mean(),
                        dados.query('ipv_2020.notna()')['ipv_2020'].mean(),
                        dados.query('ian_2020.notna()')['ian_2020'].mean()],
                ['2021', dados.query('inde_2021.notna()')['inde_2021'].mean(),
                        dados.query('iaa_2021.notna()')['iaa_2021'].mean(),
                        dados.query('ieg_2021.notna()')['ieg_2021'].mean(),
                        dados.query('ips_2021.notna()')['ips_2021'].mean(),
                        dados.query('ida_2021.notna()')['ida_2021'].mean(),
                        dados.query('ipp_2021.notna()')['ipp_2021'].mean(),
                        dados.query('ipv_2021.notna()')['ipv_2021'].mean(),
                        dados.query('ian_2021.notna()')['ian_2021'].mean()],
                ['2022', dados.query('inde_2022.notna()')['inde_2022'].mean(),
                        dados.query('iaa_2022.notna()')['iaa_2022'].mean(),
                        dados.query('ieg_2022.notna()')['ieg_2022'].mean(),
                        dados.query('ips_2022.notna()')['ips_2022'].mean(),
                        dados.query('ida_2022.notna()')['ida_2022'].mean(),
                        dados.query('ipp_2022.notna()')['ipp_2022'].mean(),
                        dados.query('ipv_2022.notna()')['ipv_2022'].mean(),
                        dados.query('ian_2022.notna()')['ian_2022'].mean()]]

qtd_medias_anos = pd.DataFrame(medias_anos, columns=['Ano', 'INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN'])
qtd_medias_anos['Ano'] = pd.to_datetime(qtd_medias_anos['Ano'], format='%Y')
qtd_medias_anos['Ano'] = qtd_medias_anos['Ano'].dt.year
qtd_medias_anos['INDE'] = qtd_medias_anos['INDE'].astype(int)
qtd_medias_anos['IAA'] = qtd_medias_anos['IAA'].astype(int)
qtd_medias_anos['IEG'] = qtd_medias_anos['IEG'].astype(int)
qtd_medias_anos['IPS'] = qtd_medias_anos['IPS'].astype(int)
qtd_medias_anos['IDA'] = qtd_medias_anos['IDA'].astype(int)
qtd_medias_anos['IPP'] = qtd_medias_anos['IPP'].astype(int)
qtd_medias_anos['IPV'] = qtd_medias_anos['IPV'].astype(int)
qtd_medias_anos['IAN'] = qtd_medias_anos['IAN'].astype(int)

graf_medias_anos = px.line(qtd_medias_anos,
                          x = 'Ano',
                          y = qtd_medias_anos.columns,
                          markers = True,
                          title='Média dos indicadores avaliativos',
                          )

graf_medias_anos.update_layout(
    xaxis_title='Ano',
    yaxis_title='Médias',
    font_family='Courier New',
    title_font_family='Roboto',
    title_font_size=22 
)

st.plotly_chart(graf_medias_anos, use_container_width=True)


bolsistas_anos = [['2020', dados[dados['bolsista_2020'] == 1]['nome'].count()],
                    ['2021', dados[dados['bolsista_2021'] == 1]['nome'].count()],
                    ['2022', dados[dados['bolsista_2022'] == 1]['nome'].count()]]

qtd_bolsistas_anos = pd.DataFrame(bolsistas_anos, columns=['Ano', 'Quantidade'])
qtd_bolsistas_anos['Ano'] = pd.to_datetime(qtd_bolsistas_anos['Ano'], format='%Y')
qtd_bolsistas_anos['Ano'] = qtd_bolsistas_anos['Ano'].dt.year
qtd_bolsistas_anos['Quantidade'] = qtd_bolsistas_anos['Quantidade'].astype(int)

dados_bolsistas_2020 = dados.loc[dados['bolsista_2020'] == 1]
dados_bolsistas_2021 = dados.loc[dados['bolsista_2021'] == 1]
dados_bolsistas_2022 = dados.loc[dados['bolsista_2022'] == 1]

bolsistas_unidades_anos = [['Centro', dados_bolsistas_2020[dados_bolsistas_2020['unidade_2020']=='Centro']['nome'].count(),
                                dados_bolsistas_2021[dados_bolsistas_2021['unidade_2021']=='Centro']['nome'].count(),
                                dados_bolsistas_2022[dados_bolsistas_2022['unidade_2022']=='Centro']['nome'].count()],
                 ['Filipinho', dados_bolsistas_2020[dados_bolsistas_2020['unidade_2020']=='Filipinho']['nome'].count(),
                                dados_bolsistas_2021[dados_bolsistas_2021['unidade_2021']=='Filipinho']['nome'].count(),
                                dados_bolsistas_2022[dados_bolsistas_2022['unidade_2022']=='Filipinho']['nome'].count()],
                 ['Cipó', dados_bolsistas_2020[dados_bolsistas_2020['unidade_2020']=='Cipó']['nome'].count(),
                                dados_bolsistas_2021[dados_bolsistas_2021['unidade_2021']=='Cipó']['nome'].count(),
                                dados_bolsistas_2022[dados_bolsistas_2022['unidade_2022']=='Cipó']['nome'].count()],
                 ['Granjinha', dados_bolsistas_2020[dados_bolsistas_2020['unidade_2020']=='Granjinha']['nome'].count(),
                                dados_bolsistas_2021[dados_bolsistas_2021['unidade_2021']=='Granjinha']['nome'].count(),
                                dados_bolsistas_2022[dados_bolsistas_2022['unidade_2022']=='Granjinha']['nome'].count()],
                 ['Outra', dados_bolsistas_2020[dados_bolsistas_2020['unidade_2020']=='Outra']['nome'].count(),
                                dados_bolsistas_2021[dados_bolsistas_2021['unidade_2021']=='Outra']['nome'].count(),
                                dados_bolsistas_2022[dados_bolsistas_2022['unidade_2022']=='Outra']['nome'].count()]]

qtd_bolsistas_unidades_anos = pd.DataFrame(bolsistas_unidades_anos, columns=['Unidade', '2020', '2021', '2022'])
qtd_bolsistas_unidades_anos['2020'] = qtd_bolsistas_unidades_anos['2020'].astype(int)
qtd_bolsistas_unidades_anos['2021'] = qtd_bolsistas_unidades_anos['2021'].astype(int)
qtd_bolsistas_unidades_anos['2022'] = qtd_bolsistas_unidades_anos['2022'].astype(int)
qtd_bolsistas_unidades_anos.set_index('Unidade', inplace = True)
qtd_bolsistas_unidades_anos = qtd_bolsistas_unidades_anos.T

col5, col6 = st.columns(2)

with col5:
    graf_bolsistas_anos = px.bar(qtd_bolsistas_anos,
                              x = 'Ano',
                              y = 'Quantidade',
                              color = 'Quantidade',
                              hover_name = 'Ano',
                              title='Total de alunos bolsistas',
                              color_continuous_scale=px.colors.sequential.Aggrnyl_r
                              )
    
    graf_bolsistas_anos.update_layout(
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=22 
    )

    st.plotly_chart(graf_bolsistas_anos, use_container_width=True)

with col6:
    graf_bolsistas_unidades_anos = px.bar(qtd_bolsistas_unidades_anos,
                              x = ['2020', '2021', '2022'],
                              y = qtd_bolsistas_unidades_anos.columns,
                              title='Quantidade de alunos bolsistas<br>por unidade',
                              )
    
    graf_bolsistas_unidades_anos.update_layout(
        xaxis_title='Ano',
        yaxis_title='Quantidade',
        font_family='Courier New',
        title_font_family='Roboto',
        title_font_size=22 
    )

    st.plotly_chart(graf_bolsistas_unidades_anos, use_container_width=True)


indices_bolsistas_anos = [['2020', dados_bolsistas_2020.query('inde_2020.notna()')['inde_2020'].mean(),
                                    dados_bolsistas_2020.query('iaa_2020.notna()')['iaa_2020'].mean(),
                                    dados_bolsistas_2020.query('ieg_2020.notna()')['ieg_2020'].mean(),
                                    dados_bolsistas_2020.query('ips_2020.notna()')['ips_2020'].mean(),
                                    dados_bolsistas_2020.query('ida_2020.notna()')['ida_2020'].mean(),
                                    dados_bolsistas_2020.query('ipp_2020.notna()')['ipp_2020'].mean(),
                                    dados_bolsistas_2020.query('ipv_2020.notna()')['ipv_2020'].mean(),
                                    dados_bolsistas_2020.query('ian_2020.notna()')['ian_2020'].mean()],
                            ['2021', dados_bolsistas_2021.query('inde_2021.notna()')['inde_2021'].mean(),
                                    dados_bolsistas_2021.query('iaa_2021.notna()')['iaa_2021'].mean(),
                                    dados_bolsistas_2021.query('ieg_2021.notna()')['ieg_2021'].mean(),
                                    dados_bolsistas_2021.query('ips_2021.notna()')['ips_2021'].mean(),
                                    dados_bolsistas_2021.query('ida_2021.notna()')['ida_2021'].mean(),
                                    dados_bolsistas_2021.query('ipp_2021.notna()')['ipp_2021'].mean(),
                                    dados_bolsistas_2021.query('ipv_2021.notna()')['ipv_2021'].mean(),
                                    dados_bolsistas_2021.query('ian_2021.notna()')['ian_2021'].mean()],
                            ['2022', dados_bolsistas_2022.query('inde_2022.notna()')['inde_2022'].mean(),
                                    dados_bolsistas_2022.query('iaa_2022.notna()')['iaa_2022'].mean(),
                                    dados_bolsistas_2022.query('ieg_2022.notna()')['ieg_2022'].mean(),
                                    dados_bolsistas_2022.query('ips_2022.notna()')['ips_2022'].mean(),
                                    dados_bolsistas_2022.query('ida_2022.notna()')['ida_2022'].mean(),
                                    dados_bolsistas_2022.query('ipp_2022.notna()')['ipp_2022'].mean(),
                                    dados_bolsistas_2022.query('ipv_2022.notna()')['ipv_2022'].mean(),
                                    dados_bolsistas_2022.query('ian_2022.notna()')['ian_2022'].mean()]]

qtd_indices_bolsistas_anos = pd.DataFrame(indices_bolsistas_anos, columns=['Ano', 'INDE', 'IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN'])
qtd_indices_bolsistas_anos['Ano'] = pd.to_datetime(qtd_indices_bolsistas_anos['Ano'], format='%Y')
qtd_indices_bolsistas_anos['Ano'] = qtd_indices_bolsistas_anos['Ano'].dt.year
qtd_indices_bolsistas_anos['INDE'] = qtd_indices_bolsistas_anos['INDE'].astype(int)
qtd_indices_bolsistas_anos['IAA'] = qtd_indices_bolsistas_anos['IAA'].astype(int)
qtd_indices_bolsistas_anos['IEG'] = qtd_indices_bolsistas_anos['IEG'].astype(int)
qtd_indices_bolsistas_anos['IPS'] = qtd_indices_bolsistas_anos['IPS'].astype(int)
qtd_indices_bolsistas_anos['IDA'] = qtd_indices_bolsistas_anos['IDA'].astype(int)
qtd_indices_bolsistas_anos['IPP'] = qtd_indices_bolsistas_anos['IPP'].astype(int)
qtd_indices_bolsistas_anos['IPV'] = qtd_indices_bolsistas_anos['IPV'].astype(int)
qtd_indices_bolsistas_anos['IAN'] = qtd_indices_bolsistas_anos['IAN'].astype(int)

graf_indices_bolsistas_anos = px.line(qtd_indices_bolsistas_anos,
                          x = 'Ano',
                          y = qtd_indices_bolsistas_anos.columns,
                          markers = True,
                          title='Média dos indicadores avaliativos dos alunos bolsistas',
                          )

graf_indices_bolsistas_anos.update_layout(
    xaxis_title='Ano',
    yaxis_title='Médias',
    font_family='Courier New',
    title_font_family='Roboto',
    title_font_size=22 
)

st.plotly_chart(graf_indices_bolsistas_anos, use_container_width=True)