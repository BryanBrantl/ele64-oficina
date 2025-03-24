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
tabs = st.tabs(["🏠 Home", "👥 Equipe", "📅 Cronograma", "📌 Atualização Semanal", "🛠️ Materiais e Métodos", "⚠️ Análise de Riscos"])

# ✅ ABA HOME
with tabs[0]:
    st.markdown("<h1 style='text-align: center;'>Bem-vindo(a) à página do Projeto de Oficina!</h1>", unsafe_allow_html=True)
    
    # Container para as 4 imagens
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("image/luizao.png", width=150)
        st.markdown("<p style='text-align: center;'>Bryan A. L. Brantl</p>", unsafe_allow_html=True)
    
    with col2:
        st.image("image/luizao.png", width=150)
        st.markdown("<p style='text-align: center;'>Joao R. Klassen</p>", unsafe_allow_html=True)
    
    with col3:
        st.image("image/luizao.png", width=150)
        st.markdown("<p style='text-align: center;'>Leonardo Amancio</p>", unsafe_allow_html=True)
    
    with col4:
        st.image("image/luizao.png", width=150)
        st.markdown("<p style='text-align: center;'>Luiz Prado Oliveira</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: justify; margin-top: 30px;'>
        <p>Esta página foi desenvolvida para apresentar o projeto de Oficina de Integração.</p>
        
        <h2>O processo de criação:</h2>
        <p>O projeto foi desenvolvido utilizando o framework Streamlit, com integração ao GitHub para facilitar o versionamento e colaboração. 
        A interface foi estilizada com HTML e CSS personalizados, garantindo uma navegação intuitiva e atraente.</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ ABA CRONOGRAMA
with tabs[2]:
    st.markdown("""
        <div class="main-content">
            <h2>Cronograma do Projeto</h2>
            <table style="width:100%; border-collapse: collapse; color: #b0b0b0;">
                <tr>
                    <th style="border: 1px solid #444; padding: 8px; background-color: #222;">Fase</th>
                    <th style="border: 1px solid #444; padding: 8px; background-color: #222;">Descrição</th>
                    <th style="border: 1px solid #444; padding: 8px; background-color: #222;">Data de Início</th>
                    <th style="border: 1px solid #444; padding: 8px; background-color: #222;">Data de Término</th>
                </tr>
                <tr>
                    <td style="border: 1px solid #444; padding: 8px;">Fase 1</td>
                    <td style="border: 1px solid #444; padding: 8px;">Definição de Requisitos</td>
                    <td style="border: 1px solid #444; padding: 8px;">DD/MM/YYYY</td>
                    <td style="border: 1px solid #444; padding: 8px;">DD/MM/YYYY</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #444; padding: 8px;">Fase 2</td>
                    <td style="border: 1px solid #444; padding: 8px;">Desenvolvimento Inicial</td>
                    <td style="border: 1px solid #444; padding: 8px;">DD/MM/YYYY</td>
                    <td style="border: 1px solid #444; padding: 8px;">DD/MM/YYYY</td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

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
