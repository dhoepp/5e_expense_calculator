# 5e Expense Calculator

Calculates monthly business income or expenses for a side project in a D&D 5e campaign (Acquisitions Incorporated ruleset).

## How to run

```
python3 calc.py
```

Optional flags:
- `-v` or `--verbose` — shows intermediate values for debugging
- `-h` or `--help` — prints a short description

## How to use

For each side project, you'll run 3 ability checks:
- The calculator generates a contest value (2d10+4) for the DM to adjudicate
- Enter Y if the check succeeds, N if it fails (default is Y)
- The number of successes determines the die rolled for that project's modifier (d8/d10/d12)

After all projects, enter a d100 roll and an optional baseline income (default 350 gold). The calculator outputs your monthly profit or expenses, rounded to the nearest 25 gold.

## Executables

Pre-built executables for Windows, macOS, and Linux are available under the **Actions** tab on GitHub. Click the latest run and download the artifact for your platform.

> Note: Windows and macOS may show a security warning since the executable is unsigned. On Windows click "More info" → "Run anyway". On Mac right-click → Open.
