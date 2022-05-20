# Renault Megane 3 RS - CAN Bus reverse engineerung

This repository constructs a dbc file for the Renault Megane 3 RS.  
This is an alternative way to using commercial tools like CANAlyzer and CANdb++ which are not available on Linux and
aren't all free.  

For the generated dbc, see the Releases page or the latest workflow run of the `main` branch.  

> __ℹ️ Note__
>
> For general info on socketcan or can tools on linux, see the `socketcan` folder in this repo [`krsche/scratchpad`](https://github.com/krsche/scratchpad)

## Getting Started

```bash
# Install dependencies
sudo apt install can-utils python3-pip
python3 -m pip install -r requirements.txt

# Generate dbc
python3 generate-dbc.py

# Start socketcan and decode via dbc
candump can0 | cantools decode --single-line renault-megane-3-rs.dbc
candump can0 | cantools monitor --single-line renault-megane-3-rs.dbc
```