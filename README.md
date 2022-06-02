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
cantools monitor -c can0 --single-line renault-megane-3-rs.dbc
```

## ToDo

### Signals I want

- ~~Steering Angle~~
- Throttle pos          (throttle_1 meaning unknown, motor required)
- Brake pressure                (factor unknown, motor required)
- ~~Brake Light Switch~~
- ~~Clutch pressed~~
- Wiper
- WheelTick
- Acceleration X
- Acceleration Y
- Acceleration Z
- Yaw rate
- RPM
- Boost pressure
- Power HP
- Torque Nm
- Sportmode
- Headlights
- ~~Parking Brake~~
- movement direction
- Magnetometer
- ESC/ABS engagement

## Msgs to ignore

0x68B
0x595
0x5EF
0x35c
0x552
0x5de
0x12e
0x242
0x29a
0x29c
0x352
0x354
0x212
0x671
0x6f8
0x5ee
0x5df
0x534
0x391
0x3f8
0x5d7
0x666
0x657
0x665
0x6fb
0x699
0x69f