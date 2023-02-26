# Template Stratégie

> **Pour utiliser ce projet il faut avoir terminé le tutoriel**

[![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://www.notion.so/Wiki-strat-gie-a97dbdf253304bbc83aab440ee57708d)


[
    ![Open in Remote - Containers](
        https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode
    )
](
    https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/godatadriven/python-devcontainer-template
)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)




## Installation

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

    ```bash
    pip install -r requirements.txt
    ```

    1.1 Use the package manager [conda](https://docs.conda.io/en/latest/) to install the requirements.

        ```bash
        conda install --file requirements.txt
        ```

        Please Use **Anaconda** or **Miniconda**

    1.2 Use poetry to install the requirements. Poetry is a dependency manager for Python that allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poerty Shell will create a virtual environment for you.

        pip install poetry
        poetry shell
        poetry install

2. Créer un fichier `.env` file à la racine du projet pour y mettre la clé secrète

    ```bash
    FMP_API_KEY= <Insert your FMP API KEY >
    BINANCE_API_KEY= <Insert your BINANCE API KEY >
    ```

3. Installer le pre-commit hook

    ```bash
    pre-commit install
    ```

4. Lancer le notebook

    ```bash
    jupyter notebook
    ```


# Pourquoi utiliser cette structure de projet ?

Cette structure s’inspire de Cookie Cutter Data Science

La qualité du code de science des données est une question d'exactitude et de reproductibilité.

Cela étant dit, il est donc préférable de commencer avec une structure propre et logique et de s'y tenir tout au long. Pour la maintenabilité, une configuration assez standardisée comme celle-ci.

```
├── .devcontainer      <- Fichiers de configuration pour VSCode
├── .github            <- Fichiers de configuration pour Github
├── README.md          <- The top-level README for developers using this project.
├── data               <- Data from third party sources.
|
├── docs               <- Documentation du projet et de la stratégie
│   ├── notebooks      <- Jupyter notebooks
│   ├── reports        <- Generated analysis as HTML, PDF, LaTeX, etc.
│
├── sandbox
│   ├── __init__.py    <- Makes src a Python module
│   ├── output         <- Output pdf de ta stratégie
│   ├── votreStrategie.ipynb        <- Jupyter de ta stratégie
│
├── src              <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module and les fonctions sont accessibles depuis n'importe quel fichier
│   ├── config.py      <- Fichier contenant les fonctions liées à la configuration
│   ├── data.py        <- Fichier contenant les fonctions liées à la récupération des données
│   ├── indicators.py  <- Fichier contenant les fonctions liées aux indicateurs
│   ├── process.py     <- Fichier contenant les fonctions liées au traitement des données
│   ├── strategy.py    <- Fichier contenant les fonctions liées à la stratégie
│   ├── test.py        <- Fichier contenant les fonctions liées aux tests
├── web                <- Github Page (https://algoets.github.io/template-strategie/web/index.html)
├── wiki               <- Wiki du projet
│
├── .pre-commit-config.yaml <- Configuration de pre-commit
├── pyproject.toml          <- Configuration de poetry
├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g. generated with `pip freeze > requirements.txt`
├── sample.env              <- Fichier d'exemple pour le fichier .env


```
## Contribution

Un pre-commit configuration a été configuré pour vérifier automatiquement chaque validation et supprime les données de sortie du bloc-notes Jupyter.


[Tâches](wiki/issues.md)

[Flux de travail](wiki/workflow.md)
