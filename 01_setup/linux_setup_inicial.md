## Setup inicial no Linux

### 1. Instalação do Python a partir do miniconda

Para um guia em vídeo sobre como instalar o *miniconda* e o *Python* no Linux/Ubuntu, ver:

[![Guia em vídeo - instalação miniconda/python](https://img.youtube.com/vi/Tk-B6Nm8qOY/0.jpg)](https://www.youtube.com/watch?v=Tk-B6Nm8qOY)

1. Ir ao site docs.conda.io e, no menu lateral, seguir o caminho `Miniconda > Linux Installers` e encontrar a versão específica para seu processador (em geral, `Python 3.11 / Miniconda3 Linux 64-bit`)

2. Rodar o script de instalação e seguir instruções:

    ```
    bash ./Miniconda3-py311-xxxxxx.sh
    ```

3. Durante a instalação, marque 'yes' para a pergunta sobre inicializar o conda. Caso contrário, será necessário executar o comando `conda init` posteriormente utilizando o comando abaixo:

    ```
    conda init "$(basename "${SHELL}")"
    ```

    obs: feche e reabra o terminal para que a inicialização tenha efeito

4. Criar um *ambiente*/*environment* Python utilizando o conda:

    ```
    conda create -n <nome_do_ambiente> python=<versão_do_python>
    ```

    **exemplo**:

    ```
    conda create -n pymusica-3.11.4 python=3.11.4
    ```

5. Ativar o ambiente criado:

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

[![Guia em vídeo - instalação atom/vscode](https://img.youtube.com/vi/I_fc9GvOAQE/0.jpg)](https://www.youtube.com/watch?v=I_fc9GvOAQE)

1. Abrir a loja de aplicativos do sistema

2. Procurar por Visual Studio e instalar*.

    *Se preferir utilizar a linha de comando, verifique a solução específica para a sua distribuição Linux:
    
    **Ubuntu, Debian e similares**:
      ```
      sudo apt update
      sudo apt install software-properties-common
      sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
      sudo apt update
      sudo apt install code
      ```

    **Fedora e similares**:

    ```
    sudo dnf install code
    ```


    **OpenSUSE:**:

    ```
    sudo zypper refresh
    sudo zypper install code
    ```

    **Arch, Manjaro e similares (tendo yay instalado)**:

    ```
    yay -S visual-studio-code-bin
    ```

3. Configuração Visual Studio:

    Instalar pacote/extensão:
    - `Python`


### 4. Instalação do Musescore e do LilyPond

1. Instalação do Musescore:

    Via loja de aplicativos da sua distribuição ou:

    
    **Ubuntu, Debian e similares**:
      ```
      sudo apt install musescore
      ```

    **Fedora e similares**:

    ```
    sudo dnf install musescore
    ```


    **OpenSUSE:**:

    ```
    sudo zypper install musescore
    ```

    **Arch, Manjaro e similares (tendo yay instalado)**:

    ```
    pamac install musescore
    ```

2. Instalação do LilyPond:

    Via loja de aplicativos da sua distribuição ou:
    
    **Ubuntu, Debian e similares**:
      ```
      sudo apt install lilypond
      ```

    **Fedora e similares**:

    ```
    sudo dnf install lilypond
    ```


    **OpenSUSE:**:

    ```
    sudo zypper install lilypond
    ```

    **Arch, Manjaro e similares (tendo yay instalado)**:

    ```
    pamac install lilypond
    ```