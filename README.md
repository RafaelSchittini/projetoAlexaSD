# Projeto Alexa

Este projeto consiste em uma skill Alexa que utiliza a API Gemini para responder perguntas dos usuários. Ele é construído usando Flask (um microframework web para Python) para servir como um endpoint para as requisições da Alexa.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado:

*   **Python 3.7 ou superior:** Verifique a versão do Python com `python --version` ou `python3 --version`. Se não tiver, instale a versão mais recente do Python 3.
*   **pip (Gerenciador de Pacotes do Python):** Normalmente vem com a instalação do Python.
*   **Uma conta na Amazon Developer Console:** Para criar e configurar a sua skill Alexa.
*   **Uma conta no Google Cloud (Google AI Studio):** Para obter uma chave de API da Gemini API.
*   **ngrok (Opcional, mas recomendado para testes locais):** Para expor o seu servidor Flask localmente à internet.

## Instalação

1.  **Clone o Repositório:**

    ```bash
    git clone [URL do seu repositório]
    cd [nome do diretório do repositório]
    ```

2.  **Criar um Ambiente Virtual:**

    Recomendamos usar um ambiente virtual para isolar as dependências do projeto.

    ```bash
    python -m venv .venv
    ```

3.  **Ativar o Ambiente Virtual:**

    *   **No Linux/macOS:**

        ```bash
        source .venv/bin/activate
        ```

    *   **No Windows (Command Prompt):**

        ```batch
        .venv\Scripts\activate.bat
        ```

    *   **No Windows (PowerShell):**

        ```powershell
        .venv\Scripts\Activate.ps1
        ```

4.  **Instalar as Dependências:**

    ```bash
    pip install flask google-generativeai python-dotenv
    ```

    ```bash
    pip install requests
    ```

5.  **Configurar a Chave da API Gemini:**

    *   **Obter a Chave:** Acesse o Google Cloud (Google AI Studio) e obtenha a sua chave de API Gemini.
    *   **Definir a Variável de Ambiente:**
        *   Defina no código sua API KEY

## Configuração da Skill Alexa

1.  **Crie uma Skill na Alexa Developer Console:**
    *   Acesse [https://developer.amazon.com/alexa/console/ask](https://developer.amazon.com/alexa/console/ask) e faça login com sua conta Amazon.
    *   Clique em "Create Skill".
    *   Escolha um nome para a sua skill (ex: "Gemini Helper").
    *   Selecione "Custom" como o tipo de skill.
    *   Escolha "Provision your own" como o método para hospedar a skill.

2.  **Configure o Modelo de Interação (Intent Schema):**
    *   Na seção "Build" da skill, defina o modelo de interação (intents, slots, utterances) conforme o exemplo fornecido nos arquivos do projeto (se houver) ou conforme as instruções nos comentários do código.
    *   Certifique-se de que o nome de invocação (invocation name) corresponda ao configurado no seu código.

3.  **Configurar o Endpoint:**
    *   Na seção "Endpoint", configure o endpoint da sua skill para o seu servidor Flask. Se você estiver usando o ngrok localmente, o endpoint será o URL HTTPS fornecido pelo ngrok. Caso contrário, será o URL do seu servidor web público.

4.  **Habilitar Testes:**
    *   Na aba "Test", habilite o teste da sua skill.

## Executar o Projeto

1.  **Execute o Servidor Flask:**

    Certifique-se de que o seu ambiente virtual está ativado.

    ```bash
    python app.py
    ```

    Se você configurou a porta para algo diferente de 5000, ajuste o comando `app.run(port=5000)` no seu código.

2.  **Expor o Servidor com ngrok (se estiver testando localmente):**

    Abra um novo terminal e execute o ngrok:

    ```bash
    ngrok http 5000  # Substitua 5000 pela porta que o seu servidor Flask está usando
    ```

    Copie o URL HTTPS fornecido pelo ngrok.

3.  **Teste a Skill Alexa:**

    *   Use o simulador na Alexa Developer Console ou fale com um dispositivo Alexa registrado na sua conta Amazon e diga:
        *   "Alexa, abra [nome de invocação da sua skill]"
        *   "Alexa, [nome de invocação da sua skill] [sua pergunta]"
