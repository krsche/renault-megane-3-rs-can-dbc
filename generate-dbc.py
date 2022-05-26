#!/usr/bin/env python3

from cantools import *

# For Bit Numbering in a message w/ big-endian / little-endian, see:
# https://cantools.readthedocs.io/en/latest/#cantools.database.can.Signal

messages = [
    db.Message(0x29C, "Wheel_Speed_Rear", 8,
               signals=[
                   db.Signal("Wheel_Speed_RL",
                             start=7,
                             length=16,
                             byte_order='big_endian',
                             is_signed=False,
                             offset=0,
                             scale=0.005,
                             minimum=0,
                             unit="km/h"),
                   db.Signal("Wheel_Speed_RR",
                             start=23,
                             length=16,
                             byte_order='big_endian',
                             is_signed=False,
                             offset=0,
                             scale=0.005,
                             minimum=0,
                             unit="km/h")
               ]),

    db.Message(0x29A, "Wheel_Speed_Front", 7,
               signals=[
                   db.Signal("Wheel_Speed_FR",
                             start=7,
                             length=16,
                             byte_order='big_endian',
                             is_signed=False,
                             offset=0,
                             scale=0.005,
                             minimum=0,
                             unit="km/h"),
                   db.Signal("Wheel_Speed_FL",
                             start=23,
                             length=16,
                             byte_order='big_endian',
                             is_signed=False,
                             offset=0,
                             scale=0.005,
                             minimum=0,
                             unit="km/h")
               ]),

    # Stellung                  Wert (hex)      Wert (dec)  Wert next best
    # Mitte:                    0x7F AA         32682       0x7fff = 32767
    # 90 links:                 0x83 C8         33736
    # 180 links:                0x87 16         34582
    # 270 links:                0x8A B3         35507
    # 360 links:                0x8E 0B         36363       0x8e00 = 36352
    # 450 links:                0x91 01
    # 470 links (anschlag):     0x92 81

    # grad / wert
    # 0         = 32682
    # 360 li    = 36363
    # 36363 - 32672 =  3691
    # 3691 / 360 = 10.252

    # grad / wert (next best)
    # 0         = 32767
    # 360 li    = 36352
    # 36352 - 32767 = 3585
    # 3585 / 360 = 9.958

    # grad / wert (next best 0 grad, real 360)
    # 0         = 32767
    # 360 li    = 36363
    # 36363 - 32767 =
    # 3596 / 360 = 9.988

    db.Message(0x0C6, "Steering", 8,
               signals=[
                   db.Signal("Steering_Angle_absolute",
                             start=7,
                             length=16,
                             byte_order='big_endian',
                             is_signed=False,
                             offset=-3276.7,
                             scale=0.1,
                             minimum=0,
                             unit="degree",
                             comment="positive is left"),
                   #    db.Signal("Steering_Angle_relative",
                   #              start=6,
                   #              length=15,
                   #              byte_order='big_endian',
                   #              is_signed=False,
                   #              offset=0,
                   #              scale=0.1,
                   #              minimum=0,
                   #              unit="degree",
                   #              comment="steering angle without direction information"),
                   #    db.Signal("Steering_direction",
                   #              start=7,
                   #              length=1,
                   #              byte_order='big_endian',
                   #              is_signed=False,
                   #              offset=0,
                   #              scale=1,
                   #              minimum=0,
                   #              unit="bool",
                   #              comment="0 is right, 1 is left"),
                   db.Signal("Steering_Angle_speed",
                             start=23,
                             length=16,
                             byte_order='big_endian',
                             is_signed=False,
                             offset=-3276.7,  # ? could be right
                             scale=0.1,  # ? could be right
                             #  minimum=0,  # ?
                             unit="degree/s",  # ? could be right
                             comment="positive is left"),
               ])
]

bus = db.database.Bus("OBD2-Port", baudrate=500000)
dbc = db.Database(messages, None, [bus])

db.dump_file(dbc, "renault-megane-3-rs.dbc", 'dbc')
