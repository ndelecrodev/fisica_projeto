# Troubleshooting

## `ModuleNotFoundError: No module named 'customtkinter'` (or `numpy`/`matplotlib`)

The virtual environment isn't active, or dependencies weren't installed. Check:

```bash
# is the environment active?
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# are dependencies installed?
pip install -r requirements.txt
```

## `ModuleNotFoundError: No module named 'tkinter'` / `_tkinter`

Tkinter isn't available in your Python installation. On Windows, reinstall Python using the official [python.org](https://www.python.org/) installer with the default options (Tkinter is bundled). On Linux, install the system package, e.g.:

```bash
sudo apt install python3-tk
```

## Window icons don't show up / error loading `.ico`

Icon paths are relative to the current working directory (e.g. `assets/icon-ico/pagina-inicial.ico`, defined in `home.py`, `page_mru_mruv.py`, and `grafico_mru_mruv.py`). Always run from the repository root:

```bash
cd fisica_projeto
python home.py
```

## "Insira valores válidos em todas as caixas de texto" ("Enter valid values in all text fields")

This message (MRU tab) appears when a required field is empty or contains a value that can't be converted to a decimal number. Check that every visible field is filled in and that the decimal separator used is a period (`.`).

## "Houve um ERRO ao calcular o MRUV" ("There was an ERROR calculating the MRUV")

Shown when none of the formulas available in `mruv.py` could be solved with the provided data. This usually means there isn't enough data — review which fields were filled against the formula table in [architecture.md](architecture.md).

## Clicking "Calcular" in the MRU tab with "Calcular Posição Final (s)" checked doesn't open any result

**Known issue in the current version of the code.** In `page_mru_mruv.py`, the `calcularMru` method calls `Mru(entry_mru_s0, entry_mru_v)` — but the `Mru` class doesn't define a constructor that accepts arguments, so this call raises an uncaught `TypeError` (the function's `try/except` block only handles `ValueError`). The correct result would be computed on the very next line, but that line is never reached. In practice this usually just shows up as a traceback in the terminal, without freezing the window. <!-- TODO: confirm whether this has already been fixed in a newer version of the code -->

## The window opens but isn't maximized / title bar icons don't appear

`self.state("zoomed")` and `iconbitmap()` with `.ico` files are more reliable on Windows. On other operating systems this behavior may vary or not work at all. <!-- TODO: confirm behavior on Linux/macOS -->

## Charts don't show up, showing "Sem valor de tempo para gerar gráficos." or "Dados insuficientes para gerar gráficos."

The charts window (`GraficoPage`) needs, at minimum, a time value (`t`) to draw any chart, and initial velocity + acceleration for the position and velocity charts. If the provided/computed data doesn't include those quantities, the corresponding charts aren't shown.
