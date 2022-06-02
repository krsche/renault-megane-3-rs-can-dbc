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
               ]),

    db.Message(0x1F6, "Brake_1", 8,
               signals=[
                   db.Signal("Is_Pressed",
                             start=19,
                             length=1,
                             byte_order='big_endian',
                             is_signed=False,
                             offset=0,
                             scale=1,
                             minimum=0,
                             unit="boolean"),
                   #    db.Signal("Wheel_Speed_FL",
                   #              start=23,
                   #              length=16,
                   #              byte_order='big_endian',
                   #              is_signed=False,
                   #              offset=0,
                   #              scale=0.005,
                   #              minimum=0,
                   #              unit="km/h")
               ]),
    db.Message(0x35C, "Pedal_States", 8,
               signals=[
                   db.Signal("Pressed_State",
                             start=47,
                             length=3,
                             byte_order='big_endian',
                             #  is_signed=False,
                             #  offset=0,
                             #  scale=1,
                             #  minimum=0,
                             #  unit="lookup",
                             choices={
                                 0x1: 'not_pressed',
                                 0x2: 'foot_over_brake',
                                 0x4: 'braking',
                             }),
                   # 0 0 0 0
                   # 8 4 2 1
                   # 0 0 1 0 = 2
                   # 0 1 0 0 = 4
                   # 1 0 0 0 = 8

                   # 0 0 0
                   # 4 2 1
                   # 0 0 1 = 1
                   # 0 1 0 = 2
                   # 1 0 0 = 4
                   #    db.Signal("Wheel_Speed_FL",
                   #              start=23,
                   #              length=16,
                   #              byte_order='big_endian',
                   #              is_signed=False,
                   #              offset=0,
                   #              scale=0.005,
                   #              minimum=0,
                   #              unit="km/h")
                   db.Signal("Clutch",  # ? or pedal
                             start=43,
                             length=2,
                             # 2B       - 2D -      35
                             # 10 1011    10 1101   11 0101
                             # 10 10      10 11     11 01
                             # 10         11        15
                             # 0 10       0 11      1 01
                             # 2         3        5
                             # 10       11        01
                             # 2         3        1
                             byte_order='big_endian',
                             is_signed=False,
                             offset=0,
                             scale=0.5,  # max 0xc8=200, min 0x00
                             minimum=0,
                             choices={
                                 1: 'open',
                                 2: 'closed',
                                 3: 'transition',
                             }),
               ]),
    db.Message(0x352, "Brake_2", 4,
               signals=[
                   db.Signal("Brake_Pressure",
                             start=31,  # maybe 19 or 23?
                             length=8,  # maybe 12 or 16?
                             byte_order='big_endian',
                             is_signed=False,
                             offset=0,
                             scale=1,  # ?
                             minimum=0,
                             unit="bar"),
                   #    db.Signal("Wheel_Speed_FL",
                   #              start=23,
                   #              length=16,
                   #              byte_order='big_endian',
                   #              is_signed=False,
                   #              offset=0,
                   #              scale=0.005,
                   #              minimum=0,
                   #              unit="km/h")
               ]),
    db.Message(0x186, "Throttle_1", 7,
               signals=[
                   db.Signal("Throttle_Pedal_pos_absolute",  # ? or body
                             start=47,
                             length=10,  # maybe 11 or 10
                             byte_order='big_endian',
                             is_signed=False,
                             offset=0,
                             # max (no kickdown) = 0xDF2 =  min 0x002; max (kickdown) = 0xFA2 #profile linear (veh off)
                             # max (no kickdown) = 0xDF2 =  min 0x002; max (kickdown) = 0xFA2
                             scale=0.1,
                             minimum=0,
                             unit="percent"),
               ]),
    db.Message(0x18A, "Throttle_2", 6,
               signals=[
                   db.Signal("Throttle_pedal_Pos_rel",  # ? or pedal
                             start=23,
                             length=8,
                             byte_order='big_endian',
                             is_signed=False,
                             offset=0,
                             scale=0.5,  # max 0xc8=200, min 0x00
                             minimum=0,
                             unit="percent"),
               ]),
    db.Message(0x4F8, "Handbrake", 7,
               signals=[
                   db.Signal("Handbrake_on",  # 0x35C last nibble of last byte changes similarly
                             start=3,
                             length=2,
                             # 01
                             # 10
                             byte_order='big_endian',
                             is_signed=False,
                             choices={
                                 1: 'false',
                                 2: 'true',
                                 3: 'unknown',
                                 4: 'unknown',
                             }),
               ]),

    # 0x12E 3. byte FD -> FC    # <-- beschleunigung Z
]

bus = db.database.Bus("OBD2-Port", baudrate=500000)
dbc = db.Database(messages, None, [bus])

db.dump_file(dbc, "renault-megane-3-rs.dbc", 'dbc')
