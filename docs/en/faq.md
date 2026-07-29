# Frequently Asked Questions (FAQ)

## What kind of application is this?

It's a **desktop** GUI application (not a website, API, or mobile app), built with CustomTkinter. It calculates quantities for Uniform Rectilinear Motion (MRU) and Uniformly Varied Rectilinear Motion (MRUV) and plots the corresponding charts.

## What units should I use?

Distance in **meters (m)**, time in **seconds (s)**, and acceleration in **meters per second squared (m/s²)**, as indicated in the MRUV tab's own interface.

## Do I need to fill in every field in the MRUV tab?

No. Leave blank the fields you don't know. The calculator tries every combination of formulas possible with the data provided and shows every result it can compute.

## Why does "Reajuste automático aplicado" sometimes appear?

This happens when a quantity (e.g. time) wasn't provided directly but could be calculated from other data — and that calculated value was then reused to obtain another quantity that depended on it (e.g. final position). The UI makes this explicit so you know that result depends on a derived value, not one you typed in.

## Can I use negative or decimal numbers?

Yes, fields accept anything Python can parse as a `float` (e.g. `-5`, `3.14`). Use a period (`.`) as the decimal separator, not a comma.

## Why don't the "Outro conteúdo" ("Other content") buttons on the home screen do anything?

They are placeholders for future content in the project. Only the "MRU e MRUV" button is currently implemented.

## Is there an API or command-line mode?

No. The application is only used through the GUI, by running `python home.py`. The `Mru` and `Mruv` classes (in `mru.py` and `mruv.py`) could, in theory, be imported and used standalone in another Python script, but that isn't a documented or officially supported usage mode for this project.

## Does the project work on Linux or macOS?

The code uses `self.state("zoomed")` to maximize the window and `.ico` files for icons — both features are more reliable on Windows. There's no confirmation of testing on Linux/macOS. <!-- TODO: confirm official Linux/macOS support -->

## Where are the calculations/formulas implemented?

In `mru.py` (MRU formulas) and `mruv.py` (MRUV formulas). See the full reference in [architecture.md](architecture.md).
