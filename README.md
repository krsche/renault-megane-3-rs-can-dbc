# Renault Megane 3 RS - CAN Bus reverse engineerung

__Gettings Started:__
```bash
# Install dependencies
python3 -m pip install -r requirements.txt

# Generate dbc
python3 generate-dbc.py

# Install can-utils on linux
sudo apt install can-utils

# Dump Can Messages (after connecting usb-can dongle)

```

# Peak PCAN - SocketCan Cheatsheet

```bash
# Download linux drivers from website

# in order to use socket-can, driver needs to be build in netdev mode
make clean
make -j12 NET=NETDEV_SUPPORT
make install

# check if kernel module is loaded / load it
lsmod | grep pcan
sudo modprobe pcan

# bring can interface up
ip link set can0 type can help
ip link set can0 type can bitrate 500000 listen-only on
ip -details link show can0
sudo ip link set can0 up

# start socketcan - candump w/ decoding via dbc
candump can0 | cantools decode --single-line renault-megane-3-rs.dbc
candump can0 | cantools monitor --single-line renault-megane-3-rs.dbc

# plot Wheel_Speed signals from saved measurement, with excluding first n lines
cat dump-example.txt | tail -n +3000 | cantools plot renault-megane-3-rs.dbc 'Wheel_Speed_*'
```