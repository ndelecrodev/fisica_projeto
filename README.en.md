# fisica_projeto — MRU/MRUV Calculator and Visualizer

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

> 🇺🇸 This README is in English. For the Portuguese version, see [README.md](README.md).

A desktop GUI application, written in Python, to calculate and visualize **Uniform Rectilinear Motion (MRU)** and **Uniformly Varied Rectilinear Motion (MRUV)** problems. The UI is built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), and charts (position, velocity, and acceleration x time) are rendered with Matplotlib.

> Note: this is a Brazilian physics project — the application's UI text (buttons, labels, dialogs) is in Portuguese. This documentation describes that UI in English but doesn't translate the running app itself.

## Table of contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Project structure](#project-structure)
- [Full documentation](#full-documentation)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python **3.11+** (developed and tested with Python 3.14.3)
- Tkinter available in your Python installation (bundled by default with the [python.org](https://www.python.org/) Windows installer)
- Python dependencies (in [`requirements.txt`](requirements.txt)):
  - `customtkinter==5.2.2` — GUI widgets
  - `numpy==2.4.6` — builds the vectors used by the charts
  - `matplotlib==3.10.9` — chart rendering

Dependency management uses **pip + venv** (no Poetry, Conda, or Pipenv).

## Installation

```bash
git clone https://github.com/ndelecrodev/fisica_projeto.git
cd fisica_projeto

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Detailed guide, including install verification and common troubleshooting: [docs/en/installation.md](docs/en/installation.md).

## Quick start

Run from the repository root (icons use relative paths):

```bash
python home.py
```

The main window opens maximized. Click **"MRU e MRUV"** to open the calculator, pick a tab (MRU or MRUV), check what you want to calculate, fill in the fields, and click **Calcular** (Calculate). The result opens in a window with a **Ver Gráficos** (View Charts) button.

Full usage guide with examples: [docs/en/usage.md](docs/en/usage.md).

## Project structure

```
projeto_fisica/
├── assets/                # icons (.ico used at runtime, .png reference files)
├── docs/
│   ├── pt/                 # full documentation, Portuguese
│   └── en/                 # full documentation, English
├── interface/               # reserved folder, currently empty
├── home.py                  # application entry point
├── home_page.py              # home page (menu)
├── page_mru_mruv.py          # MRU/MRUV calculator page
├── mru.py                    # MRU formulas
├── mruv.py                    # MRUV formulas
├── grafico_mru_mruv.py        # charts window (Matplotlib)
├── requirements.txt
└── LICENSE
```

Details of each module and the page flow: [docs/en/architecture.md](docs/en/architecture.md).

## Full documentation

The complete documentation lives in [`docs/en/`](docs/en/):

- [Installation](docs/en/installation.md)
- [Usage](docs/en/usage.md)
- [Architecture](docs/en/architecture.md)
- [FAQ](docs/en/faq.md)
- [Troubleshooting](docs/en/troubleshooting.md)

## Contributing

There is no formal contribution guide (`CONTRIBUTING.md`) in this repository. To contribute:

1. Fork the repository.
2. Create a branch for your change (`git checkout -b my-feature`).
3. Commit your changes and open a Pull Request describing what changed and why.

## License

Distributed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for the full text.
