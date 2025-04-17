import streamlit as st

# 🔧 Configuração da página
st.set_page_config(page_title="Projeto BioMove", layout="wide")

# 🎨 Estilização com CSS customizado
st.markdown("""
<style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .nav-bar {
        display: flex;
        justify-content: space-around;
        background-color: #1e1e1e;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .nav-item {
        padding: 10px 20px;
        border-radius: 8px;
        color: white;
        text-decoration: none;
        font-weight: bold;
        background-color: #444;
    }
    .nav-item:hover {
        background-color: #666;
    }
    .nav-active {
        background-color: #ff4b4b;
    }
    h1, h2, h3 {
        text-align: center;
        font-weight: bold;
        color: #ffffff;
    }
    p, li {
        font-size: 16px;
        color: #bbbbbb;
    }
    .main-content {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 📁 Criação das abas
abas = st.tabs(["Home", "BioMove", "Atualização Semanal", "Relatórios", "Cronograma"])

# 🏠 ABA HOME
with abas[0]:
    st.markdown("""<h1>Home</h1>""", unsafe_allow_html=True)

    # 👤 Perfis dos integrantes com imagens personalizadas
    colunas = st.columns(4)
    fotos = ["image/foto_01.png", "image/foto_02.png", "image/foto_03.png", "image/foto_04.png"]
    for col, foto in zip(colunas, fotos):
        with col:
            st.image(foto, width=100)
            st.markdown("""
                <div style='text-align: center;'>
                    <p><b>Nome completo</b></p>
                    <p>RA</p>
                    <p>Período</p>
                    <p>Contato</p>
                </div>
            """, unsafe_allow_html=True)

    # 📄 Seções com textos e imagens/gifs
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("image/gif1.gif", caption="GIF 1", use_column_width=True)
    with col2:
        st.markdown("""
            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed urna amet.</p>
        """)

    col3, col4 = st.columns([2, 1])
    with col3:
        st.markdown("""
            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed urna amet. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisi malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.</p>
        """)
    with col4:
        st.image("image/gif2.gif", caption="GIF 2", use_column_width=True)

    # 🔀 Mais conteúdo fictício
    st.markdown("""
        <p>Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed urna amet.</p>
        <p>Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisi malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.</p>
    """)

# 🔬 ABA BioMove
with abas[1]:
    st.markdown("""<h1>BioMove</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vel augue sed arcu tincidunt fermentum. Duis at ligula sed purus faucibus porttitor.</p>""", unsafe_allow_html=True)

# 📜 ABA Atualização Semanal
with abas[2]:
    st.markdown("""<h1>Atualização Semanal</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dignissim luctus orci at iaculis.</p>""", unsafe_allow_html=True)

# 📊 ABA Relatórios
with abas[3]:
    st.markdown("""<h1>Relatórios</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sodales augue at sapien tincidunt, eget tincidunt justo gravida.</p>""", unsafe_allow_html=True)

# 🗓️ ABA Cronograma
with abas[4]:
    st.markdown("""<h1>Cronograma</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras at vehicula mauris, non ullamcorper lorem. Curabitur vitae erat velit.</p>""", unsafe_allow_html=True)
