# Arquitetura

Visão geral de como o código está organizado.

## Visão geral

O projeto é uma aplicação **desktop de interface gráfica** (não há backend, API ou banco de dados). É construída com [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (uma camada estilizada sobre o Tkinter da biblioteca padrão do Python) e usa Matplotlib embutido em widgets Tkinter para desenhar gráficos.

A aplicação segue um padrão simples de **páginas registradas em um dicionário**, trocadas via `pack()`/`pack_forget()` dentro da janela raiz — não há um framework de roteamento.

## Estrutura de diretórios

```
projeto_fisica/
├── assets/
│   ├── icon-ico/        # ícones .ico usados em tempo de execução (iconbitmap)
│   └── icon-png/        # versões .png dos ícones (não referenciadas no código)
├── docs/
│   ├── pt/               # esta documentação, em português
│   └── en/               # documentação equivalente, em inglês
├── interface/             # pasta vazia (reservada, sem uso atual)
├── home.py                # ponto de entrada — janela raiz e navegação
├── home_page.py            # página inicial (menu)
├── page_mru_mruv.py        # página da calculadora de MRU/MRUV
├── mru.py                  # fórmulas de MRU
├── mruv.py                 # fórmulas de MRUV
├── grafico_mru_mruv.py     # janela de gráficos (Matplotlib)
├── requirements.txt
├── LICENSE
├── README.md / README.en.md
└── .gitattributes
```

> A pasta `interface/` existe no repositório mas está vazia — não há indicação no código de para que ela é usada. <!-- TODO: confirm propósito da pasta interface/ -->

## Módulos

### `home.py` — ponto de entrada

Define a classe `Home(ctk.CTk)`, a janela raiz da aplicação. No construtor:

- Ativa o tema escuro (`ctk.set_appearance_mode("dark")`) e o esquema de cores `dark-blue`.
- Maximiza a janela (`self.state("zoomed")`) — comportamento específico do Tkinter no Windows.
- Instancia todas as páginas em um dicionário `self._paginas` e exibe a página `"inicial"`.

O método `browse(destination)` esconde todas as páginas e exibe apenas a solicitada, atualizando o título da janela e o ícone (`iconbitmap`).

O módulo é executado diretamente ao rodar `python home.py` (não há bloco `if __name__ == "__main__":` — `app = Home(); app.mainloop()` roda no nível do módulo).

### `home_page.py` — `HomePage`

`ctk.CTkFrame` com o menu principal. Recebe um callback `on_navigate` do `Home` para trocar de página sem depender diretamente da classe raiz. Contém um botão funcional ("MRU e MRUV") e três botões de placeholder ("Outro conteúdo") sem `command` associado.

### `page_mru_mruv.py` — `MruMruvPage`

A tela principal da calculadora, organizada em um `ctk.CTkTabview` com duas abas: **MRU** e **MRUV**. Principais responsabilidades:

- Monta dinamicamente os campos de entrada (`_build_aba_mru`, `_build_aba_mruv`) de acordo com as opções (checkboxes) marcadas pelo usuário (`checkBoxesMru`, `checkBoxesMruv`).
- Lê e valida os campos, delega os cálculos às classes `Mru`/`Mruv`, e mostra o resultado em uma janela `ctk.CTkToplevel` (`_dialog_resposta_mru`, `_dialog_resposta_mruv`) ou uma janela de erro (`_dialog_erro`).
- Abre a janela de gráficos (`GraficoPage`) a partir do botão "Ver Gráficos".
- Na aba MRUV, tenta **todas as fórmulas compatíveis** com os campos preenchidos e aplica um "reajuste automático": se uma grandeza intermediária (ex.: tempo) foi calculada e ainda falta outra grandeza que depende dela (ex.: posição final), recalcula usando o valor obtido.

### `mru.py` — `Mru`

Classe simples, sem estado (não define `__init__`), com métodos que implementam as fórmulas do Movimento Retilíneo Uniforme:

| Método | Fórmula | Parâmetros |
|---|---|---|
| `calcularPosicaoFinal(t, s0, v)` | `s = s0 + v·t` | tempo, posição inicial, velocidade |
| `calcular_tempo(s, s0, v)` | `t = (s - s0) / v` | posição final, posição inicial, velocidade |
| `calcular_tempo_espaco(espaco, v)` | `t = Δs / v` | espaço percorrido, velocidade |
| `calcular_velocidade_espaco(espaco, t)` | `v = Δs / t` | espaço percorrido, tempo |
| `calcular_velocidade(s0, t, s)` | `v = (s - s0) / t` | posição inicial, tempo, posição final |

### `mruv.py` — `Mruv`

Classe com estado, inicializada com `Mruv(s0=None, s=None, v0=None, v=None, a=None, t=None)`. Cada método calcula uma grandeza a partir das demais, levantando `ValueError` quando os dados necessários não foram fornecidos (ou levariam a uma divisão por zero / raiz negativa):

| Método | Fórmula | Requer |
|---|---|---|
| `calcularPosicao()` | `s = s0 + v0·t + a·t²/2` | s0, v0, a, t |
| `calcularVelocidadeFinal()` | `v = v0 + a·t` | v0, a, t |
| `calcularAceleracaoPorTempo()` | `a = (v - v0) / t` | v, v0, t (t ≠ 0) |
| `calcularAceleracaoPorDistancia()` | `a = (v² - v0²) / (2·Δs)` (Torricelli) | v, v0, s, s0 (Δs ≠ 0) |
| `calcularTempo()` | `t = (v - v0) / a` | v, v0, a (a ≠ 0) |
| `calcularVelocidadeInicialPeloTempo()` | `v0 = v - a·t` | v, a, t |
| `calcularVelocidadeInicialPorDistancia()` | `v0 = √(v² - 2·a·Δs)` | v, a, s, s0 |
| `calcularEspacoPercorrido()` | 3 variantes, dependendo dos dados disponíveis | v0+a+t, ou v+v0+a, ou v0+v+t |
| `calcularAceleracaoPeloEspacoPercorrido(espaco)` | `a = (v² - v0²) / (2·Δs)` ou `a = 2·(Δs - v0·t)/t²` | v+v0, ou v0+t |
| `calcularVelocidadeFinalPeloEspacoPercorrido(espaco)` | `v = √(v0² + 2·a·Δs)` | v0, a |
| `calcularVelocidadeInicialPeloEspacoPercorrido(espaco)` | `v0 = √(v² - 2·a·Δs)` | v, a |
| `calcularTempoPeloEspacoPercorrido(espaco)` | soma/subtração ou equação de Bhaskara (`calcular_tempo_mruv_espaco`) | v0+v, ou a+v0 |

`page_mru_mruv.py` usa essas classes chamando cada método dentro de um `try/except`, coletando quantos resultados forem possíveis, em vez de exigir um conjunto fixo de campos preenchidos.

### `grafico_mru_mruv.py` — `GraficoPage`

`ctk.CTkToplevel` que recebe o modo (`"mru"` ou `"mruv"`) e os valores calculados. Resolve os valores de `t`, `v0`, `v`, `a`, `s0` (no MRU, `a` é sempre `0`), gera um vetor de tempo com `numpy.linspace` e desenha até três gráficos (posição, velocidade, aceleração x tempo) em abas separadas, usando `matplotlib.figure.Figure` embutido via `FigureCanvasTkAgg`. Se não houver tempo disponível ou nenhum gráfico puder ser montado, exibe uma mensagem de aviso em vez dos gráficos.

## Fluxo de dados (resumo)

```
home.py (Home)
 └── HomePage ──on_navigate──▶ MruMruvPage
                                   ├── Mru()  (aba MRU)
                                   ├── Mruv() (aba MRUV)
                                   └── GraficoPage (numpy + matplotlib)
```

Não há persistência de dados (arquivos, banco de dados) nem chamadas de rede — todo o estado vive na memória do processo enquanto a janela está aberta.
