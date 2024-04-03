import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Home",
        page_icon="🏠",
    )

    st.title("Bem-vindo ao ambiente da Passos Mágicos")

    st.markdown(
        """
A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.

A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.

Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.

    """
    )

    col1, col2, col3 = st.columns(3)

    with col2:
      st.image('data/passos-magicos.png', use_column_width=True)

    st.write('Texto e imagens via <https://passosmagicos.org.br/>.')

if __name__ == "__main__":
    run()