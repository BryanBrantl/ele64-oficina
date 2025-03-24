import streamlit as st

# 🔥 Definir configurações da página
st.set_page_config(page_title="Projeto de Oficina", layout="wide")

# 🔥 Estilo personalizado com CSS
st.markdown("""
    <style>
        /* Estilo da barra de navegação */
        .navbar {
            background-color: #1c1c1c;
            padding: 15px;
            border-radius: 12px;
            display: flex;
            justify-content: center;
            gap: 30px;
        }
        .navbar a {
            color: #ffffff;
            text-decoration: none;
            font-size: 18px;
            padding: 8px 16px;
            border-radius: 8px;
            transition: background-color 0.3s;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .navbar a:hover {
            background-color: #ff4b4b;
            color: #ffffff;
        }
        .active {
            background-color: #ff4b4b;
            color: #ffffff;
        }
        /* Estilo do conteúdo principal */
        .main-content {
            background-color: #0e0e0e;
            color: #ffffff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
        }
        h1 {
            color: #ffffff;
            font-size: 42px;
            font-weight: bold;
        }
        h2 {
            color: #ffffff;
            font-size: 32px;
            font-weight: bold;
            margin-top: 20px;
        }
        p {
            font-size: 18px;
            line-height: 1.6;
            color: #b0b0b0;
        }
    </style>
""", unsafe_allow_html=True)

# 🔥 Barra de navegação com botões
menu = st.markdown("""
    <div class="navbar">
        <a href="?page=home" class="active">🏠 Home</a>
        <a href="?page=equipe">👥 Equipe</a>
        <a href="?page=cronograma">📅 Cronograma</a>
        <a href="?page=atualizacao">📌 Atualização</a>
        <a href="?page=materiais">🛠️ Materiais e Métodos</a>
        <a href="?page=riscos">⚠️ Análise de Riscos</a>
    </div>
""", unsafe_allow_html=True)

# 🔥 Definir página com base na URL
query_params = st.query_params
page = query_params.get("page", ["home"])[0]

# 🔥 Página Home
if page == "home":
    st.markdown("""
        <div class="main-content">
            <h1>Bem-vindo(a) à minha página pessoal!</h1>
            <p>Esta página foi desenvolvida para apresentar o projeto de Oficina de Integração, realizado por:</p>
            <ul>
                <li>Bryan A. L. Brantl</li>
                <li>Joao R. Klassen</li>
                <li>Leonardo Amancio</li>
                <li>Luiz Prado Oliveira</li>
            </ul>
            <h2>O processo de criação:</h2>
            <p>O projeto foi desenvolvido utilizando o framework Streamlit, com integração ao GitHub para facilitar o versionamento e colaboração. 
            A interface foi estilizada com HTML e CSS personalizados, garantindo uma navegação intuitiva e atraente.</p>
        </div>
    """, unsafe_allow_html=True)

# 🔥 Página Equipe
elif page == "equipe":
    st.title("Equipe")
    st.write("""
    - **Bryan A. L. Brantl**  
    - **Joao R. Klassen**  
    - **Leonardo Amancio**  
    - **Luiz Prado Oliveira**  
    """)

# 🔥 Página Cronograma
elif page == "cronograma":
    st.title("Cronograma")
    st.write("""
    | Fase | Descrição | Data de Início | Data de Término |
    |-------|-----------|----------------|-----------------|
    | Fase 1 | Definição de requisitos | DD/MM/YYYY | DD/MM/YYYY |
    | Fase 2 | Desenvolvimento inicial | DD/MM/YYYY | DD/MM/YYYY |
    | Fase 3 | Testes e ajustes | DD/MM/YYYY | DD/MM/YYYY |
    | Fase 4 | Entrega final | DD/MM/YYYY | DD/MM/YYYY |
    """)

# 🔥 Página Atualização Semanal
elif page == "atualizacao":
    st.title("Atualização Semanal")
    semana = st.text_input("Semana", "")
    atualizacao = st.text_area("Atualização", "")
    if st.button("Salvar Atualização"):
        st.success("Atualização salva com sucesso!")

# 🔥 Página Materiais e Métodos
elif page == "materiais":
    st.title("Materiais e Métodos")
    st.write("""
    **Materiais Utilizados:**  
    - ESP32  
    - Display TFT 1.28" (GC9A01)  
    - Sensores  
    - Módulos de comunicação sem fio  

    **Métodos:**  
    - Programação em C/C++  
    - Uso de bibliotecas específicas para ESP32  
    - Comunicação SPI  
    """)

# 🔥 Página Análise de Riscos
elif page == "riscos":
    st.title("Análise de Riscos")
    st.write("""
    **Riscos Técnicos:**  
    - Falha na comunicação com sensores  
    - Problemas de compatibilidade com bibliotecas  

    **Riscos de Projeto:**  
    - Atrasos no cronograma  
    - Falta de componentes críticos  

    **Mitigação:**  
    - Testes antecipados  
    - Backup de componentes e bibliotecas  
    - Revisões semanais  
    """)

