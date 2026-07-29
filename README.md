# fisica_projeto — Calculadora e Visualizador de MRU/MRUV

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

> 🇧🇷 Este README está em português. Para a versão em inglês, veja [README.en.md](README.en.md).

Aplicação desktop com interface gráfica, feita em Python, para calcular e visualizar problemas de **Movimento Retilíneo Uniforme (MRU)** e **Movimento Retilíneo Uniformemente Variado (MRUV)**. A interface é construída com [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) e os gráficos (posição, velocidade e aceleração x tempo) são renderizados com Matplotlib.

## Sumário

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso rápido](#uso-rápido)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Documentação completa](#documentação-completa)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Requisitos

- Python **3.11+** (desenvolvido e testado com Python 3.14.3)
- Tkinter disponível na instalação do Python (incluso por padrão no instalador do [python.org](https://www.python.org/) no Windows)
- Dependências Python (em [`requirements.txt`](requirements.txt)):
  - `customtkinter==5.2.2` — widgets da interface gráfica
  - `numpy==2.4.6` — geração dos vetores usados nos gráficos
  - `matplotlib==3.10.9` — renderização dos gráficos

Gerenciamento de dependências feito com **pip + venv** (sem Poetry, Conda ou Pipenv).

## Instalação

```bash
git clone https://github.com/ndelecrodev/fisica_projeto.git
cd fisica_projeto

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Guia detalhado, incluindo verificação da instalação e solução de problemas comuns: [docs/pt/instalacao.md](docs/pt/instalacao.md).

## Uso rápido

Execute a partir da raiz do repositório (os ícones usam caminhos relativos):

```bash
python home.py
```

A janela principal abre maximizada. Clique em **"MRU e MRUV"** para acessar a calculadora, escolha a aba (MRU ou MRUV), marque o que deseja calcular, preencha os campos e clique em **Calcular**. O resultado abre em uma janela com um botão **Ver Gráficos**.

Guia de uso completo, com exemplos: [docs/pt/uso.md](docs/pt/uso.md).

## Estrutura do projeto

```
projeto_fisica/
├── assets/                # ícones (.ico usados em runtime, .png de referência)
├── docs/
│   ├── pt/                 # documentação completa em português
│   └── en/                 # documentação completa em inglês
├── interface/               # pasta reservada, atualmente vazia
├── home.py                  # ponto de entrada da aplicação
├── home_page.py              # página inicial (menu)
├── page_mru_mruv.py          # página/calculadora de MRU e MRUV
├── mru.py                    # fórmulas de MRU
├── mruv.py                    # fórmulas de MRUV
├── grafico_mru_mruv.py        # janela de gráficos (Matplotlib)
├── requirements.txt
└── LICENSE
```

Detalhes de cada módulo e o fluxo entre as páginas: [docs/pt/arquitetura.md](docs/pt/arquitetura.md).

## Documentação completa

Toda a documentação detalhada está em [`docs/pt/`](docs/pt/):

- [Instalação](docs/pt/instalacao.md)
- [Uso](docs/pt/uso.md)
- [Arquitetura](docs/pt/arquitetura.md)
- [FAQ](docs/pt/faq.md)
- [Solução de problemas](docs/pt/troubleshooting.md)

## Contribuindo

Não há um guia formal de contribuição (`CONTRIBUTING.md`) neste repositório. Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua alteração (`git checkout -b minha-feature`).
3. Faça commit das suas mudanças e abra um Pull Request descrevendo o que foi alterado e por quê.

## Licença

Distribuído sob a licença **Apache License 2.0** — veja o arquivo [LICENSE](LICENSE) para o texto completo.
