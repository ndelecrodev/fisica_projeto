# Installation

Complete guide to set up the environment and install the project's dependencies.

## Prerequisites

- **Python 3.11 or higher** (`numpy` and `matplotlib` at the pinned versions require at least this version). The development environment uses Python 3.14.3.
- **Tkinter** available in your Python installation. On Windows, the official [python.org](https://www.python.org/) installer already bundles Tkinter. On some Linux distributions you need to install it separately (e.g. `sudo apt install python3-tk`).
- Git (optional, only needed to clone the repository).

This project uses **pip + venv** for dependency management. Poetry, Conda, and Pipenv are not supported.

## 1. Clone the repository

```bash
git clone https://github.com/ndelecrodev/fisica_projeto.git
cd fisica_projeto
```

## 2. Create the virtual environment

```bash
python -m venv venv
```

## 3. Activate the virtual environment

**Linux/macOS:**

```bash
source venv/bin/activate
```

**Windows (cmd/PowerShell):**

```bash
venv\Scripts\activate
```

Once active, your terminal prompt is prefixed with `(venv)`.

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

This installs the three libraries the code actually imports:

| Package | Version | Used for |
|---|---|---|
| `customtkinter` | 5.2.2 | GUI widgets (windows, buttons, tabs, text fields) |
| `numpy` | 2.4.6 | Building the time vectors used by the charts |
| `matplotlib` | 3.10.9 | Rendering the charts (position x time, velocity x time, acceleration x time) embedded in the UI |

<!-- TODO: confirm whether the project should support Python < 3.11 ; the pinned numpy/matplotlib versions don't. -->

## 5. Verify the installation

```bash
python -c "import customtkinter, numpy, matplotlib; print('OK')"
```

If the output is `OK`, the environment is ready. Continue with [usage.md](usage.md) to learn how to run the application.

## Deactivating the virtual environment

```bash
deactivate
```
