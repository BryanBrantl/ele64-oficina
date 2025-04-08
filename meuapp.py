import streamlit as st

# 🔥 Definir configurações da página
st.set_page_config(page_title="Projeto de Oficina", layout="wide")

# 🔥 Estilo personalizado com CSS
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .main-content {
            background-color: #1e1e1e;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
            color: #ffffff;
        }
        h1, h2 {
            text-align: center;
            font-weight: bold;
            color: #ffffff;
        }
        h1 { font-size: 42px; }
        h2 { font-size: 32px; margin-top: 20px; }
        p, li {
            font-size: 18px;
            line-height: 1.6;
            color: #bbbbbb;
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
        .info-box {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.6);
            margin-top: 20px;
            color: #ffffff;
        }
        .info-box h2 {
            color: #ff4b4b;
            font-size: 28px;
        }
        .info-box p {
            color: #bbbbbb;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# 🔥 Criação das abas
tabs = st.tabs(["Home", "Projetos", "Cronograma", "Atualização Semanal", "Materiais e Métodos", "Análise de Riscos"])

# ✅ ABA HOME
with tabs[0]:
    st.markdown("<h1 style='text-align: center;'>Bem-vindo(a) ao Projeto de Oficina!</h1>", unsafe_allow_html=True)
    
    # Container para as 4 imagens
    colunas = st.columns(4)
    nomes = ["Bryan A. L. Brantl", "Joao R. Klassen", "Leonardo Amancio", "Luiz Prado Oliveira"]
    periodos = ["5º", "7º", "6º", "7º"]
    emails = ["bryan.brantl@email.com", "joao.klassen@email.com", "leonardo.amancio@email.com", "luiz.oliveira@email.com"]
    telefones = ["(31) 98765-4321", "(31) 91234-5678", "(31) 99876-5432", "(31) 92345-6789"]
    imagens = ["image/foto_01.png", "image/foto_02.png", "image/foto_03.png", "image/foto_04.png"]

    for i, col in enumerate(colunas):
        with col:
            st.image(imagens[i], width=500)  # 🔥 Imagem maior
            st.markdown(f"""
                <div style='text-align: center;'>
                    <p><b style='color: #ffffff; font-size: 18px;'>{nomes[i]}</b></p>
                    <p style='color: #bbbbbb; font-size: 16px;'>Engenharia Eletrônica - {periodos[i]} Período</p>
                    <p style='color: #bbbbbb; font-size: 14px;'>{emails[i]}</p>
                    <p style='color: #bbbbbb; font-size: 14px;'>{telefones[i]}</p>
                </div>
            """, unsafe_allow_html=True)
    
    # 🔥 Bloco de informações com contraste melhorado
    st.markdown("""
    <div style="
        background-color: #1e1e1e; 
        padding: 20px; 
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
        margin-top: 20px;
    ">
        <h2 style="color: #ffffff;">O Processo de Criação</h2>
        <p style="color: #bbbbbb;">Desenvolvido com Streamlit e integrado ao GitHub para versionamento e colaboração. Interface estilizada com HTML/CSS personalizados.</p>
    </div>
    """, unsafe_allow_html=True)



# ✅ ABA PROJETOS
with tabs[1]:
    st.markdown("""
    <div class="main-content">
        <h2>Projetos</h2>
        <h3 style="color: #ff4b4b;">Proposta 01: Monitoramento Remoto de Saúde</h3>
        <p><b style="color: #ffffff;">Problema:</b> Em regiões afastadas, o acesso a serviços médicos é limitado. Pacientes crônicos precisam de acompanhamento constante.</p>
        <p><b style="color: #ffffff;">Solução:</b> Dispositivo vestível monitora sinais vitais (oxigenação, batimentos cardíacos, temperatura) e transmite via LoRa/GSM/WiFi para centros de saúde.</p>
        <h3 style="color: #ff4b4b;">Integração</h3>
        <ul>
            <li><b style="color: #ffffff;">Eletrônica:</b> Sensores biomédicos e circuito de aquisição de sinais.</li>
            <li><b style="color: #ffffff;">Eletrônica Digital:</b> Processamento de dados e envio de alertas.</li>
            <li><b style="color: #ffffff;">Microcontroladores:</b> ESP32 ou STM32 para comunicação remota.</li>
            <li><b style="color: #ffffff;">Computação:</b> Plataforma Web/App para monitoramento.</li>
        </ul>
        <h3 style="color: #ff4b4b;">Proposta 2</h3>
        <h3 style="color: #ff4b4b;">Proposta 3</h3>
    </div>
    """, unsafe_allow_html=True)

with tabs[2]:
    st.markdown("""
    <div class="main-content">
        <h2>Cronograma do Projeto – Carrinho Controlado por EMG</h2>

        <h3 style="color: #ff4b4b;">Entregáveis</h3>
        <ul>
            <li><b>11/04:</b> Entregável #1 – Plano de Projeto</li>
            <li><b>11/04:</b> Entregável #2 – Blog do Projeto (link inicial)</li>
            <li><b>23/05:</b> Entregável #3 – Projeto e testes de Hardware</li>
            <li><b>04/07:</b> Entregável #4 – Projeto e testes de Software (relatório, vídeo e blog)</li>
            <li><b>11/07:</b> Entregável #5 – Integração e Demonstração para banca</li>
        </ul>

        <h3 style="color: #ff4b4b;">Atividades</h3>
        <table style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #333;"><th>Atividade</th><th>Responsável</th><th>Início</th><th>Fim</th><th>Duração</th></tr>
            <tr><td>Montagem do carrinho</td><td>Leonardo</td><td>08/04</td><td>10/04</td><td>2 dias</td></tr>
            <tr><td>Projeto circuito EMG</td><td>Bryan</td><td>10/04</td><td>13/04</td><td>3 dias</td></tr>
            <tr><td>Simulação circuito EMG</td><td>Bryan</td><td>13/04</td><td>14/04</td><td>1 dia</td></tr>
            <tr><td>Montagem EMG protoboard</td><td>João</td><td>15/04</td><td>17/04</td><td>2 dias</td></tr>
            <tr><td>Calibração do sinal EMG</td><td>João</td><td>17/04</td><td>18/04</td><td>1 dia</td></tr>
            <tr><td>Montagem dos motores</td><td>Luiz</td><td>18/04</td><td>19/04</td><td>1 dia</td></tr>
            <tr><td>Leitura do sinal EMG</td><td>João</td><td>19/04</td><td>21/04</td><td>2 dias</td></tr>
            <tr><td>Interpretação sinais EMG</td><td>Bryan</td><td>22/04</td><td>24/04</td><td>2 dias</td></tr>
            <tr><td>Controle do carrinho</td><td>Luiz</td><td>25/04</td><td>28/04</td><td>3 dias</td></tr>
            <tr><td>Testes com voluntário</td><td>Todos</td><td>29/04</td><td>30/04</td><td>2 dias</td></tr>
            <tr><td>Ajustes finais</td><td>Todos</td><td>01/05</td><td>02/05</td><td>2 dias</td></tr>
        </table>

        <h3 style="color: #ff4b4b; margin-top: 40px;">Resumo por Responsável</h3>
        <ul>
            <li><b>Leonardo:</b> 2 dias</li>
            <li><b>Bryan:</b> 6 dias</li>
            <li><b>João:</b> 5 dias</li>
            <li><b>Luiz:</b> 4 dias</li>
            <li><b>Todos:</b> 4 dias</li>
            <li><b>Total do Projeto:</b> 21 dias</li>
        </ul>
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
