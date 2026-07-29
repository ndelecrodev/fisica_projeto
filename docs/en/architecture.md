# Architecture

Overview of how the code is organized.

## Overview

The project is a **desktop GUI application** (there is no backend, API, or database). It's built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (a styled layer on top of Python's standard Tkinter) and uses Matplotlib embedded in Tkinter widgets to draw charts.

The app follows a simple **pages registered in a dictionary** pattern, swapped via `pack()`/`pack_forget()` inside the root window — there is no routing framework.

## Directory structure

```
projeto_fisica/
├── assets/
│   ├── icon-ico/        # .ico icons used at runtime (iconbitmap)
│   └── icon-png/        # .png versions of the icons (not referenced in code)
├── docs/
│   ├── pt/               # this documentation, in Portuguese
│   └── en/               # equivalent documentation, in English
├── interface/             # empty folder (reserved, currently unused)
├── home.py                # entry point — root window and navigation
├── home_page.py            # home/menu page
├── page_mru_mruv.py        # MRU/MRUV calculator page
├── mru.py                  # MRU formulas
├── mruv.py                 # MRUV formulas
├── grafico_mru_mruv.py     # charts window (Matplotlib)
├── requirements.txt
├── LICENSE
├── README.md / README.en.md
└── .gitattributes
```

> The `interface/` folder exists in the repository but is empty — there's no indication in the code of what it's meant for. <!-- TODO: confirm the purpose of the interface/ folder -->

## Modules

### `home.py` — entry point

Defines `Home(ctk.CTk)`, the app's root window. In its constructor:

- Enables dark mode (`ctk.set_appearance_mode("dark")`) and the `dark-blue` color theme.
- Maximizes the window (`self.state("zoomed")`) — a Tkinter behavior specific to Windows.
- Instantiates every page into a `self._paginas` dictionary and shows the `"inicial"` page.

The `browse(destination)` method hides all pages and shows only the requested one, updating the window title and icon (`iconbitmap`).

The module is run directly when executing `python home.py` (there is no `if __name__ == "__main__":` guard — `app = Home(); app.mainloop()` runs at module level).

### `home_page.py` — `HomePage`

A `ctk.CTkFrame` with the main menu. Receives an `on_navigate` callback from `Home` to switch pages without depending directly on the root class. Contains one functional button ("MRU e MRUV") and three placeholder buttons ("Outro conteúdo") with no `command` attached.

### `page_mru_mruv.py` — `MruMruvPage`

The main calculator screen, organized in a `ctk.CTkTabview` with two tabs: **MRU** and **MRUV**. Main responsibilities:

- Dynamically builds the input fields (`_build_aba_mru`, `_build_aba_mruv`) based on which checkboxes the user selects (`checkBoxesMru`, `checkBoxesMruv`).
- Reads and validates the fields, delegates the math to the `Mru`/`Mruv` classes, and shows the result in a `ctk.CTkToplevel` window (`_dialog_resposta_mru`, `_dialog_resposta_mruv`) or an error window (`_dialog_erro`).
- Opens the charts window (`GraficoPage`) from the "Ver Gráficos" button.
- In the MRUV tab, it tries **every compatible formula** for the filled fields and applies an "automatic adjustment": if an intermediate quantity (e.g. time) was computed and another quantity still depends on it (e.g. final position), it recomputes using the derived value.

### `mru.py` — `Mru`

A simple, stateless class (no `__init__` defined) whose methods implement the Uniform Rectilinear Motion formulas:

| Method | Formula | Parameters |
|---|---|---|
| `calcularPosicaoFinal(t, s0, v)` | `s = s0 + v·t` | time, initial position, velocity |
| `calcular_tempo(s, s0, v)` | `t = (s - s0) / v` | final position, initial position, velocity |
| `calcular_tempo_espaco(espaco, v)` | `t = Δs / v` | distance traveled, velocity |
| `calcular_velocidade_espaco(espaco, t)` | `v = Δs / t` | distance traveled, time |
| `calcular_velocidade(s0, t, s)` | `v = (s - s0) / t` | initial position, time, final position |

### `mruv.py` — `Mruv`

A stateful class, initialized as `Mruv(s0=None, s=None, v0=None, v=None, a=None, t=None)`. Each method computes one quantity from the others, raising `ValueError` when the required data wasn't supplied (or would lead to a division by zero / negative square root):

| Method | Formula | Requires |
|---|---|---|
| `calcularPosicao()` | `s = s0 + v0·t + a·t²/2` | s0, v0, a, t |
| `calcularVelocidadeFinal()` | `v = v0 + a·t` | v0, a, t |
| `calcularAceleracaoPorTempo()` | `a = (v - v0) / t` | v, v0, t (t ≠ 0) |
| `calcularAceleracaoPorDistancia()` | `a = (v² - v0²) / (2·Δs)` (Torricelli) | v, v0, s, s0 (Δs ≠ 0) |
| `calcularTempo()` | `t = (v - v0) / a` | v, v0, a (a ≠ 0) |
| `calcularVelocidadeInicialPeloTempo()` | `v0 = v - a·t` | v, a, t |
| `calcularVelocidadeInicialPorDistancia()` | `v0 = √(v² - 2·a·Δs)` | v, a, s, s0 |
| `calcularEspacoPercorrido()` | 3 variants, depending on the data available | v0+a+t, or v+v0+a, or v0+v+t |
| `calcularAceleracaoPeloEspacoPercorrido(espaco)` | `a = (v² - v0²) / (2·Δs)` or `a = 2·(Δs - v0·t)/t²` | v+v0, or v0+t |
| `calcularVelocidadeFinalPeloEspacoPercorrido(espaco)` | `v = √(v0² + 2·a·Δs)` | v0, a |
| `calcularVelocidadeInicialPeloEspacoPercorrido(espaco)` | `v0 = √(v² - 2·a·Δs)` | v, a |
| `calcularTempoPeloEspacoPercorrido(espaco)` | sum/subtraction, or the quadratic formula (`calcular_tempo_mruv_espaco`) | v0+v, or a+v0 |

`page_mru_mruv.py` uses these classes by calling each method inside a `try/except`, collecting as many results as it can, instead of requiring one fixed set of filled fields.

### `grafico_mru_mruv.py` — `GraficoPage`

A `ctk.CTkToplevel` that receives the mode (`"mru"` or `"mruv"`) and the computed values. It resolves `t`, `v0`, `v`, `a`, `s0` (in MRU mode, `a` is always `0`), builds a time vector with `numpy.linspace`, and draws up to three charts (position, velocity, acceleration x time) in separate tabs, using `matplotlib.figure.Figure` embedded via `FigureCanvasTkAgg`. If no time value is available, or no chart can be built, it shows a warning message instead of the charts.

## Data flow (summary)

```
home.py (Home)
 └── HomePage ──on_navigate──▶ MruMruvPage
                                   ├── Mru()  (MRU tab)
                                   ├── Mruv() (MRUV tab)
                                   └── GraficoPage (numpy + matplotlib)
```

There is no data persistence (files, database) and no network calls — all state lives in process memory while the window is open.
