# Instalação

Guia completo para preparar o ambiente e instalar as dependências do projeto.

## Pré-requisitos

- **Python 3.11 ou superior** (as dependências `numpy` e `matplotlib` exigem no mínimo essa versão). O ambiente de desenvolvimento usa Python 3.14.3.
- **Tkinter** disponível na instalação do Python. No Windows e no instalador oficial do [python.org](https://www.python.org/) o Tkinter já vem incluído. Em algumas distribuições Linux é necessário instalar o pacote separadamente (ex.: `sudo apt install python3-tk`).
- Git (opcional, apenas para clonar o repositório).

Este projeto usa **pip + venv** para gerenciar dependências. Não há suporte a Poetry, Conda ou Pipenv.

## 1. Clonar o repositório

```bash
git clone https://github.com/ndelecrodev/fisica_projeto.git
cd fisica_projeto
```

## 2. Criar o ambiente virtual

```bash
python -m venv venv
```

## 3. Ativar o ambiente virtual

**Linux/macOS:**

```bash
source venv/bin/activate
```

**Windows (cmd/PowerShell):**

```bash
venv\Scripts\activate
```

Quando o ambiente estiver ativo, o prompt do terminal passa a exibir o prefixo `(venv)`.

## 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

Isso instala as três bibliotecas que o código efetivamente importa:

| Pacote | Versão | Uso no projeto |
|---|---|---|
| `customtkinter` | 5.2.2 | Widgets da interface gráfica (janelas, botões, abas, campos de texto) |
| `numpy` | 2.4.6 | Geração dos vetores de tempo usados nos gráficos |
| `matplotlib` | 3.10.9 | Renderização dos gráficos (posição x tempo, velocidade x tempo, aceleração x tempo) embutidos na interface |

<!-- TODO: confirm se o projeto deve suportar Python < 3.11 ; numpy/matplotlib nas versões fixadas não suportam. -->

## 5. Verificar a instalação

```bash
python -c "import customtkinter, numpy, matplotlib; print('OK')"
```

Se a saída for `OK`, o ambiente está pronto. Prossiga para [uso.md](uso.md) para aprender a executar a aplicação.

## Desativando o ambiente virtual

```bash
deactivate
```
