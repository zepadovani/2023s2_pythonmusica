## Setup inicial no Windows

### 1. [opcional] Gerenciador de pacotes do Windows: **chocolatey**

É recomendado instalar um gerenciador de pacotes no seu sistema operacional. Embora estejamos habituados a instalar aplicativos utilizando ícones e aplicativos, utilizar um gerenciador pela linha de comando facilita gerenciar aplicativos e ferramentas que serão utilizadas ao longo das aulas. Em síntese, um gerenciador de pacotes permite instalar e atualizar aplicativos pela linha de comando, gerenciando de maneira mais prática/rápida sua versão, instalação e desinstalação.

No Windows, recomendamos o gerenciador **chocolatey**:

Para um guia em vídeo sobre como instalar o *chocolatey*, ver:

[![Guia em vídeo - instalação chocolatey](https://img.youtube.com/vi/eHoh_ptUkmw/0.jpg)](https://www.youtube.com/watch?v=eHoh_ptUkmw)

1. Instalar a versão mais recente do *Powershell*, específica para seu sistema, a partir deste site:
[https://github.com/PowerShell/PowerShell/releases]

(obs: ao instalar, marque a opção que permite que adiciona o menu 'Open Here'/'Abrir Aqui' no Explorer)

2. Instalar *chocolatey* a partir do site: [https://chocolatey.org/install]

    2.1 Abrir PowerShell em modo admnistrador

    2.2 Executar o comando `Get-ExecutionPolicy`. Se retornar: `Restricted`, execute o comando `Set-ExecutionPolicy RemoteSigned `

    2.3 Executar o script de instalação do *chocolatey*:

    ```
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```

### 2. Instalação do Python a partir do miniconda

Para um guia em vídeo sobre como instalar o *miniconda* e o *Python* no windows, ver:

[![Guia em vídeo - instalação miniconda/python](https://img.youtube.com/vi/qt9UGKVSXnY/0.jpg)](https://www.youtube.com/watch?v=qt9UGKVSXnY)

1. Instalar o **miniconda** pelo PowerShell (em modo admnistrador):

    ```
    choco install miniconda3
    ```

    Caso não tenha instalado o chocolatey, será necessário baixar o instalador manual do miniconda e rodar o executável manualmente.


2. Abrir o terminal do miniconda e inicializar o conda para o PowerShell:

    ```
    conda init powershell
    ```

    obs: feche e reabra o shell (sempre em modo admnitrador) para que isso faça efeito

3. Criar um *ambiente*/*environment* Python utilizando o conda:

    ```
    conda create -n <nome_do_ambiente> python=<versão_do_python>
    ```

    **exemplo**:

    ```
    conda create -n pymusica-3.11.4 python=3.11.4
    ```

4. Ativar o ambiente criado:

    ```
    conda activate pymusica-3.11.4
    ```

5. Intalação do Jupyter

    ```
    pip install jupyter
    ```

6. Configurar o kernel Jupyter (que possibilita utilizarmos o ambiente criado em modo interativo):

    ```
    python -m ipykernel install --user --name pymusica-3.11.4 --display-name "pymusica-3.11.4"
    ```

7. Testando/rodando o Jpyter:

    ```
    jupyter notebook
    ```

8. Instalação de pacotes (exemplo com `numpy`):

    ```
    pip install numpy
    ```

### 3. Instalação e configuração do Visual Studio

Para um guia em vídeo sobre como instalar e configurar o Visual Studio, ver (ignore a parte do vídeo sobre o Atom, editor que foi descontinuado):

[![Guia em vídeo - instalação atom/vscode](https://img.youtube.com/vi/YxqoFTBYQLE/0.jpg)](https://www.youtube.com/watch?v=YxqoFTBYQLE)

1. Abrir PowerShell em modo admnistrador

2. Instalação do Visual Studio Code:

    ```
    choco install vscode -y
    ```

3. Configuração Visual Studio:

      Instalar pacote/extensão:
      - `Python`

### 4. Instalação do Musescore e do LilyPond

(OBS: Caso não tenha instalado o chocolatey, será necessário baixar o instalador manual do Musescore e do Lilypond e rodar os instaladores manualmente.)

1. Instalação do Musescore:
    
    ```
    choco install musescore -y
    ```

2. Instalação do LilyPond:

    ```
    choco install lilypond -y
    ```