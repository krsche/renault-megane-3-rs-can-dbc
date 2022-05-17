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
ip link list
ip link set can0 type can help
ip link set can0 type can bitrate 500000 listen-only on
ip -details link show can0
sudo ip link set can0 up

# start socketcan - candump w/ decoding via dbc
candump can0 | cantools decode --single-line renault-megane-3-rs.dbc
candump can0 | cantools monitor --single-line renault-megane-3-rs.dbc

# plot Wheel_Speed signals from saved measurement, with excluding first n lines
cat dump-example.txt | tail -n +3000 | cantools plot renault-megane-3-rs.dbc 'Wheel_Speed_*'

# monitor messages 'trace style'
can_viewer.py -c can0 -i socketcan
```

# Replay
## Bring up vcan0
```bash
# Check kernel module loaded / which are avail & load
lsmod | grep vcan
find /lib/modules/$(uname -r) -type f -name '*.ko*'
sudo modprobe vcan

# add vcan0 interface & bring up
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

## Start Replay
When measurement was captures as ASCII (plain text output from candump) it first needs to be converted to the compact 
format.  
There is a tool for that called `asc2log` but didn't work for me.
Instead I used this awk command, which should do the same.

> __candump output:__  
> `(000.000000)  can0  12E   [8]  C8 7F FD 7F F0 FF FF 00`  
>
> __compact format:__ this is used when capturing via `candump -L somename.txt`  
> `(000.000000) can0 12E#C87FFD7FF0FFFF00`  

```bash
cat heimfahrt-1.txt | awk '{print ""$1" "$2" "$3"#"$5$6$7$8$9$10$11$12 }' | canplayer vcan0=can0
```
