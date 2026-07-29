# Usage

How to run the application and use the MRU/MRUV calculator.

## Running the application

With the virtual environment active and dependencies installed (see [installation.md](installation.md)), run from the repository root:

```bash
python home.py
```

> **Important:** run this from the project root. Window icons are loaded with relative paths (e.g. `assets/icon-ico/pagina-inicial.ico`), so running the script from another directory means the icons won't be found.

The main window opens maximized, in dark mode, showing the **Home Page**.

## Navigation

The Home Page shows content buttons. Currently only the **"MRU e MRUV"** button is functional and leads to the calculator. The other buttons ("Outro conteúdo" / "Other content") exist in the UI but have no action attached — they are placeholders for future content.

Inside the calculator page there are two tabs: **MRU** and **MRUV**. Each tab has a **Voltar** (Back) button that returns to the Home Page.

## MRU tab (Uniform Rectilinear Motion)

1. Check **only one** of the three checkboxes, depending on what you want to calculate:
   - **Calcular Posição Final (s)** (Calculate Final Position) — asks for initial position (s0), velocity (v), and time (t).
   - **Calcular Velocidade (v)** (Calculate Velocity) — asks whether you have the distance traveled (Δs). If yes, it asks for Δs and time; if no, it asks for initial position, final position, and time.
   - **Calcular Tempo (t)** (Calculate Time) — same Δs logic: with Δs it asks for velocity; without Δs it asks for initial position, final position, and velocity.
2. Fill in the fields shown (decimal numbers, use `.` as the separator).
3. Press **Enter** in any field or click **Calcular** (Calculate).
4. The result appears in a pop-up window, with a **Ver Gráficos** (View Charts) button to open the position/velocity/acceleration x time charts.

If any field is empty or contains a non-numeric value, an error window appears: *"Insira valores válidos em todas as caixas de texto"* ("Enter valid values in all text fields").

## MRUV tab (Uniformly Varied Rectilinear Motion)

1. State whether you have the **Espaço Percorrido (Δs)** (distance traveled) by checking **Sim** (Yes) or **Não** (No) — only one of the two.
2. Fill in whichever fields apply to your problem. **Leave blank the fields you don't know** — the calculator automatically figures out which quantities can be derived from the values provided.
3. Expected units: distance in **meters**, time in **seconds**, acceleration in **m/s²**.
4. Click **Calcular** (or press Enter, where applicable).

The calculator tries every MRUV formula compatible with the values provided and shows **all possible results** — not just one. When an intermediate result (e.g. time) is required to compute another quantity (e.g. final position) and wasn't provided directly, the calculator reuses the value it just computed and flags this in the result window, under **"Reajuste automático aplicado"** ("Automatic adjustment applied").

If no combination of formulas can be solved with the given data, the message *"Houve um ERRO ao calcular o MRUV"* ("There was an ERROR calculating the MRUV") is shown.

As in the MRU tab, the result is shown in a pop-up window with a **Ver Gráficos** button.

## Charts

The **Ver Gráficos** button opens a new window with tabs containing (whenever the required data is available):

- **s x t** — position over time
- **v x t** — velocity over time
- **a x t** — acceleration over time (dashed line)

In MRU mode, acceleration is always fixed at `0`. Result windows (MRU, MRUV, error) close automatically after a delay: **60 seconds** for result windows and **10 seconds** for error windows.

## Practical example (MRU)

Calculating the final position with `s0 = 0`, `v = 10` (m/s), `t = 5` (s):

1. Go to the **MRU** tab.
2. Check **Calcular Posição Final (s)**.
3. Fill in: Posição Inicial = `0`, Velocidade = `10`, Tempo = `5`.
4. Click **Calcular** → expected result: `Posição Final: 50.00`.

<!-- TODO: confirm whether this specific calculation can currently fail silently — see docs/en/troubleshooting.md -->
