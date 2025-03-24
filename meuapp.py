import streamlit as st

# 🔥 Definir configurações da página (primeira linha obrigatoriamente)
st.set_page_config(page_title="Projeto de Oficina", layout="wide")

# 🔥 Estilo personalizado com CSS
st.markdown("""
    <style>
        /* Estilo para o título principal */
        h1 {
            color: #ffffff;
            font-size: 42px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        h2 {
            color: #ffffff;
            font-size: 32px;
            font-weight: bold;
            margin-top: 20px;
        }
        p, li {
            font-size: 18px;
            line-height: 1.6;
            color: #b0b0b0;
        }
        .main-content {
            background-color: #0e0e0e;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
        }
    </style>
""", unsafe_allow_html=True)

# 🔥 Criação das abas
tabs = st.tabs(["Home", "Projetos", "Cronograma", " Atualização Semanal", "Materiais e Métodos", "Análise de Riscos"])

# ✅ ABA HOME
with tabs[0]:
    st.markdown("<h1 style='text-align: center;'>Bem-vindo(a) à página do Projeto de Oficina!</h1>", unsafe_allow_html=True)
    
    # Container para as 4 imagens
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("image/luizao.png", width=150)
        st.markdown("""
        <div style='text-align: center;'>
            <p style='font-weight: bold; margin-bottom: 5px;'>Bryan A. L. Brantl</p>
            <p style='font-size: 14px; margin: 2px;'>Engenharia Eletrônica</p>
            <p style='font-size: 14px; margin: 2px;'>5º Período</p>
            <p style='font-size: 14px; margin: 2px;'>bryan.brantl@email.com</p>
            <p style='font-size: 14px; margin: 2px;'>(31) 98765-4321</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("image/luizao.png", width=150)
        st.markdown("""
        <div style='text-align: center;'>
            <p style='font-weight: bold; margin-bottom: 5px;'>Joao R. Klassen</p>
            <p style='font-size: 14px; margin: 2px;'>Engenharia Eletrônica</p>
            <p style='font-size: 14px; margin: 2px;'>7º Período</p>
            <p style='font-size: 14px; margin: 2px;'>joao.klassen@email.com</p>
            <p style='font-size: 14px; margin: 2px;'>(31) 91234-5678</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.image("image/luizao.png", width=150)
        st.markdown("""
        <div style='text-align: center;'>
            <p style='font-weight: bold; margin-bottom: 5px;'>Leonardo Amancio</p>
            <p style='font-size: 14px; margin: 2px;'>Engenharia Eletrônica</p>
            <p style='font-size: 14px; margin: 2px;'>6º Período</p>
            <p style='font-size: 14px; margin: 2px;'>leonardo.amancio@email.com</p>
            <p style='font-size: 14px; margin: 2px;'>(31) 99876-5432</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.image("image/luizao.png", width=150)
        st.markdown("""
        <div style='text-align: center;'>
            <p style='font-weight: bold; margin-bottom: 5px;'>Luiz Prado Oliveira</p>
            <p style='font-size: 14px; margin: 2px;'>Engenharia Eletrônica</p>
            <p style='font-size: 14px; margin: 2px;'>7º Período</p>
            <p style='font-size: 14px; margin: 2px;'>luiz.oliveira@email.com</p>
            <p style='font-size: 14px; margin: 2px;'>(31) 92345-6789</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: justify; margin-top: 30px;'>
        <h2>O processo de criação:</h2>
        <p>O projeto foi desenvolvido utilizando o framework Streamlit, com integração ao GitHub para facilitar o versionamento e colaboração. 
        A interface foi estilizada com HTML e CSS personalizados, garantindo uma navegação intuitiva e atraente.</p>
    </div>
    """, unsafe_allow_html=True)
with tabs[1]:
st.markdown("""
    **Objetivo**: Acompanhar pacientes em tempo real, garantindo atendimento rápido em emergências.
""")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Sensores Utilizados")
    st.write("- Oxímetro (SpO2)")
    st.write("- ECG (Batimentos Cardíacos)")
    st.write("- Termômetro (Temperatura Corporal)")

with col2:
    st.subheader("Tecnologias de Comunicação")
    st.write("- LoRa (Long Range)")
    st.write("- GSM (Cobertura Celular)")

st.subheader("Fluxo de Dados")
    
# ✅ ABA ATUALIZAÇÃO SEMANAL
with tabs[3]:
    st.markdown("<h2>Atualização Semanal</h2>", unsafe_allow_html=True)
    semana = st.text_input("Semana", "")
    atualizacao = st.text_area("Atualização", "")
    if st.button("Salvar Atualização"):
        st.success("Atualização salva com sucesso!")

# ✅ ABA MATERIAIS E MÉTODOS
with tabs[4]:
    st.markdown("""
        <div class="main-content">
            <h2>Materiais e Métodos</h2>
            <ul>
                <li>ESP32</li>
                <li>Display TFT 1.28" (GC9A01)</li>
                <li>Sensores</li>
                <li>Módulos de comunicação sem fio</li>
            </ul>
            <p><b>Métodos:</b> Programação em C/C++, uso de bibliotecas específicas para ESP32 e comunicação SPI.</p>
        </div>
    """, unsafe_allow_html=True)

# ✅ ABA ANÁLISE DE RISCOS
with tabs[5]:
    st.markdown("""
        <div class="main-content">
            <h2>Análise de Riscos</h2>
            <p><b>Riscos Técnicos:</b></p>
            <ul>
                <li>Falha na comunicação com sensores</li>
                <li>Problemas de compatibilidade com bibliotecas</li>
            </ul>
            <p><b>Riscos de Projeto:</b></p>
            <ul>
                <li>Atrasos no cronograma</li>
                <li>Falta de componentes críticos</li>
            </ul>
            <p><b>Mitigação:</b> Testes antecipados, backup de componentes e revisões semanais.</p>
        </div>
    """, unsafe_allow_html=True)
