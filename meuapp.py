import streamlit as st

# 🔥 Definir configurações da página
st.set_page_config(page_title="Projeto de Oficina", layout="wide")

# 🔥 Estilo personalizado com CSS
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
        }
        .main-content {
            background-color: #1e1e1e;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
        }
        h1, h2, h3 {
            text-align: center;
            font-weight: bold;
            color: #ff4b4b; /* Vermelho para destaque */
        }
        h1 { font-size: 42px; }
        h2 { font-size: 32px; margin-top: 20px; }
        h3 { font-size: 24px; }
        p, li {
            font-size: 18px;
            line-height: 1.6;
            color: #b0b0b0; /* Cinza claro para contraste */
        }
        .nav-bar {
            display: flex;
            justify-content: space-around;
            background-color: #1e1e1e;
            padding: 10px;
            border-radius: 8px;
        }
        .nav-item {
            padding: 10px 20px;
            border-radius: 8px;
            color: #ffffff;
            text-decoration: none;
            font-weight: bold;
        }
        .nav-item:hover {
            background-color: #333;
        }
        .nav-active {
            background-color: #ff4b4b;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# 🔥 Criação das abas
tabs = st.tabs(["Home", "Projetos", "Cronograma", "Atualização Semanal", "Materiais e Métodos", "Análise de Riscos"])

# ✅ ABA HOME
with tabs[0]:
    st.markdown("<h1>Bem-vindo(a) ao Projeto de Oficina!</h1>", unsafe_allow_html=True)
    
    # Container para as 4 imagens
    colunas = st.columns(4)
    nomes = ["Bryan A. L. Brantl", "Joao R. Klassen", "Leonardo Amancio", "Luiz Prado Oliveira"]
    periodos = ["5º", "7º", "6º", "7º"]
    emails = ["bryan.brantl@email.com", "joao.klassen@email.com", "leonardo.amancio@email.com", "luiz.oliveira@email.com"]
    telefones = ["(31) 98765-4321", "(31) 91234-5678", "(31) 99876-5432", "(31) 92345-6789"]
    
    for i, col in enumerate(colunas):
        with col:
            st.image("image/luizao.png", width=120)  # 🔥 Tamanho da imagem ajustado
            st.markdown(f"""
                <div style='text-align: center; color: #b0b0b0;'>
                    <p><b>{nomes[i]}</b></p>
                    <p>Engenharia Eletrônica - {periodos[i]} Período</p>
                    <p>{emails[i]}</p>
                    <p>{telefones[i]}</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="main-content">
        <h2>O Processo de Criação</h2>
        <p>Desenvolvido com Streamlit e integrado ao GitHub para versionamento e colaboração. Interface estilizada com HTML/CSS personalizados.</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ ABA PROJETOS
with tabs[1]:
    st.markdown("""
    <div class="main-content">
        <h2>Projetos</h2>
        <h3>Monitoramento Remoto de Saúde</h3>
        <p><b>Problema:</b> Em regiões afastadas, o acesso a serviços médicos é limitado. Pacientes crônicos precisam de acompanhamento constante.</p>
        <p><b>Solução:</b> Dispositivo vestível monitora sinais vitais (oxigenação, batimentos cardíacos, temperatura) e transmite via LoRa/GSM para centros de saúde.</p>
        <h3>Integração</h3>
        <ul>
            <li><b>Eletrônica:</b> Sensores biomédicos e circuito de aquisição de sinais.</li>
            <li><b>Eletrônica Digital:</b> Processamento de dados e envio de alertas.</li>
            <li><b>Microcontroladores:</b> ESP32 ou STM32 para comunicação remota.</li>
            <li><b>Computação:</b> Plataforma Web/App para monitoramento.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ✅ ABA CRONOGRAMA
with tabs[2]:
    st.markdown("""
    <div class="main-content">
        <h2>Cronograma</h2>
        <p>🔴 <b>Janeiro:</b> Definição de escopo e planejamento.</p>
        <p>🟠 <b>Fevereiro:</b> Desenvolvimento de hardware e firmware.</p>
        <p>🟡 <b>Março:</b> Testes e integração.</p>
        <p>🟢 <b>Abril:</b> Validação e documentação final.</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ ABA ATUALIZAÇÃO SEMANAL
with tabs[3]:
    st.markdown("""
    <div class="main-content">
        <h2>Atualização Semanal</h2>
        <p><b>Semana 1:</b> Implementação inicial do hardware.</p>
        <p><b>Semana 2:</b> Configuração do firmware.</p>
        <p><b>Semana 3:</b> Comunicação com sensores.</p>
        <p><b>Semana 4:</b> Testes e ajustes.</p>
    </div>
    """, unsafe_allow_html=True)

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
        <h3>Riscos Técnicos</h3>
        <ul>
            <li>Falha na comunicação com sensores.</li>
            <li>Problemas de compatibilidade com bibliotecas.</li>
        </ul>
        <h3>Riscos de Projeto</h3>
        <ul>
            <li>Atrasos no cronograma.</li>
            <li>Falta de componentes críticos.</li>
        </ul>
        <p><b>Mitigação:</b> Testes antecipados, backup de componentes e revisões semanais.</p>
    </div>
    """, unsafe_allow_html=True)
