## Setup inicial no macOS

### 1. [opcional] Gerenciador de pacotes do macOS: **homebrew**

É recomendado instalar um gerenciador de pacotes no seu sistema operacional. Embora estejamos habituados a instalar aplicativos utilizando ícones e aplicativos, utilizar um gerenciador pela linha de comando facilita gerenciar aplicativos e ferramentas que serão utilizadas ao longo das aulas. Em síntese, um gerenciador de pacotes permite instalar e atualizar aplicativos pela linha de comando, gerenciando de maneira mais prática/rápida sua versão, instalação e desinstalação.

No macOS, recomendamos o gerenciador **homebrew**:

Para um guia em vídeo sobre como instalar o *homebrew*, ver:

[![Guia em vídeo - instalação homebrew](https://img.youtube.com/vi/cI1dQXoZeqA/0.jpg)](https://www.youtube.com/watch?v=cI1dQXoZeqA)

1. [opcional] Instalar o iTerm:

    Baixar e instalar o aplicativo a partir do endereço: [https://iterm2.com/]

2. Abrir o terminal (o iTerm ou o Terminal, do próprio macOS)

3. Copiar o script de instalação do homebrew no site [https://brew.sh/]

4. Colar no terminal e executar para realizar a instalação:

    ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```


### 2. Instalação do Python a partir do miniconda

Para um guia em vídeo sobre como instalar o *miniconda* e o *Python* no macOS, ver:

[![Guia em vídeo - instalação miniconda/python](https://img.youtube.com/vi/cisrgY2G5IE/0.jpg)](https://www.youtube.com/watch?v=cisrgY2G5IE)

1. Instalar o **miniconda** pelo terminal utilizando o homebrew:

    ```
    brew install --cask miniconda
    ```

2. Inicializar o conda para o terminal em uso:

    ```
    conda init "$(basename "${SHELL}")"
    ```

    obs: feche e reabra o shell para que isso faça efeito

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
    python -m ipykernel install --user --name pymusica-3.11.4  --display-name "pymusica-3.11.4 "
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

[![Guia em vídeo - instalação atom/vscode](https://img.youtube.com/vi/sZ9efYWqpE8/0.jpg)](https://www.youtube.com/watch?v=sZ9efYWqpE8)

1. Abrir o Terminal/iTerm

2. Instalação do Visual Studio Code:

    ```
    brew install --cask visual-studio-code
    ```

3. Configuração Visual Studio:

      Instalar pacote/extensão:
      - `Python`

### 4. Instalação do Musescore e do LilyPond

(OBS: Caso não tenha instalado o homebrew, será necessário baixar o Musescore e o Lilypond e instalar esses aplicativos manualmente)

1. Instalação do Musescore:
    
    ```
    brew install --cask musescore
    ```

2. Instalação do LilyPond:

    ```
    brew install lilypond
    ```