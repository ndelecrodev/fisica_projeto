# Solução de Problemas (Troubleshooting)

## `ModuleNotFoundError: No module named 'customtkinter'` (ou `numpy`/`matplotlib`)

O ambiente virtual não está ativado ou as dependências não foram instaladas. Confira:

```bash
# ambiente ativo?
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# dependências instaladas?
pip install -r requirements.txt
```

## `ModuleNotFoundError: No module named 'tkinter'` / `_tkinter`

O Tkinter não está disponível na sua instalação do Python. No Windows, reinstale o Python usando o instalador oficial do [python.org](https://www.python.org/) marcando a opção padrão (o Tkinter vem incluído). No Linux, instale o pacote do sistema, por exemplo:

```bash
sudo apt install python3-tk
```

## Os ícones das janelas não aparecem / erro ao carregar `.ico`

Os caminhos dos ícones são relativos ao diretório de trabalho (ex.: `assets/icon-ico/pagina-inicial.ico`, definidos em `home.py`, `page_mru_mruv.py` e `grafico_mru_mruv.py`). Execute sempre a partir da raiz do repositório:

```bash
cd fisica_projeto
python home.py
```

## "Insira valores válidos em todas as caixas de texto"

Essa mensagem (aba MRU) aparece quando algum campo obrigatório está vazio ou contém um valor que não pode ser convertido para número decimal. Verifique se todos os campos exibidos foram preenchidos e se o separador decimal usado é o ponto (`.`).

## "Houve um ERRO ao calcular o MRUV"

Aparece quando nenhuma das fórmulas disponíveis em `mruv.py` conseguiu ser resolvida com os dados informados. Normalmente significa que faltam dados suficientes — revise quais campos foram preenchidos considerando a tabela de fórmulas em [arquitetura.md](arquitetura.md).

## Clicar em "Calcular" na aba MRU com "Calcular Posição Final (s)" marcado não abre nenhum resultado

**Problema conhecido na versão atual do código.** Em `page_mru_mruv.py`, o método `calcularMru` chama `Mru(entry_mru_s0, entry_mru_v)` — mas a classe `Mru` não define um construtor que aceite argumentos, então essa chamada gera um `TypeError` que não é capturado (o bloco `try/except` da função só trata `ValueError`). O resultado correto seria calculado logo na linha seguinte, mas ela nunca é alcançada. Na prática, isso costuma aparecer apenas como um traceback no terminal, sem travar a janela. <!-- TODO: confirm se esse comportamento já foi corrigido em uma versão mais recente do código -->

## A janela abre, mas não fica maximizada / os ícones da barra de título não aparecem

`self.state("zoomed")` e `iconbitmap()` com arquivos `.ico` são recursos mais confiáveis no Windows. Em outros sistemas operacionais, esse comportamento pode variar ou não funcionar. <!-- TODO: confirm comportamento em Linux/macOS -->

## Os gráficos não aparecem, aparece "Sem valor de tempo para gerar gráficos." ou "Dados insuficientes para gerar gráficos."

A janela de gráficos (`GraficoPage`) precisa, no mínimo, de um valor de tempo (`t`) para desenhar qualquer gráfico, e de velocidade inicial + aceleração para os gráficos de posição e velocidade. Se os dados informados/calculados não incluírem essas grandezas, os gráficos correspondentes não são exibidos.
