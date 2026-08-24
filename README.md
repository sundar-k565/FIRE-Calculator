# FIRE Calculator Suite

A desktop financial-planning application for estimating long-term goals in Indian rupees. The interface includes calculators for:

- Financial Independence / Retire Early (FIRE)
- Home purchases and loan repayments
- Wedding savings
- Children's education, wedding, and maintenance goals

Each calculator displays its results alongside a Matplotlib chart.

## Requirements

- Python 3.9 or newer
- Tkinter
- NumPy
- Matplotlib

Tkinter is included with most Python installations. On Linux, you may need to install it through your system package manager (for example, `sudo apt install python3-tk` on Ubuntu/Debian).

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```powershell
.venv\Scripts\activate
```

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python FIRE-Calc.py
```

Enter your assumptions in a calculator tab and select its calculate button to view the estimates and chart.

## Disclaimer

This application is for educational and illustrative purposes only. Its projections depend on the assumptions entered and should not be treated as financial advice.
