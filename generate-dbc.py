import cantools

# For Bit Numbering in a message w/ big-endian / little-endian, see:
# https://cantools.readthedocs.io/en/latest/#cantools.database.can.Signal

messages = [
    cantools.db.Message(0x29C, "Wheel_Speed_Rear", 8,
        signals=[
            cantools.db.Signal("Wheel_Speed_RL",
                                start=7,
                                length=16,
                                byte_order='big_endian',
                                is_signed=False,
                                offset=0,
                                scale=0.005,
                                minimum=0,
                                unit="km/h"),
            cantools.db.Signal("Wheel_Speed_RR",
                                start=23,
                                length=16,
                                byte_order='big_endian',
                                is_signed=False,
                                offset=0,
                                scale=0.005,
                                minimum=0,
                                unit="km/h")
        ]),

    cantools.db.Message(0x29A, "Wheel_Speed_Front", 7,
        signals=[
            cantools.db.Signal("Wheel_Speed_FR",
                                start=7,
                                length=16,
                                byte_order='big_endian',
                                is_signed=False,
                                offset=0,
                                scale=0.005,
                                minimum=0,
                                unit="km/h"),
            cantools.db.Signal("Wheel_Speed_FL",
                                start=23,
                                length=16,
                                byte_order='big_endian',
                                is_signed=False,
                                offset=0,
                                scale=0.005,
                                minimum=0,
                                unit="km/h")
        ])
]

bus = cantools.db.database.Bus("OBD2-Port", baudrate=500000)
db = cantools.db.Database(messages, None, [bus])

cantools.db.dump_file(db, "renault-megane-3-rs.dbc", 'dbc')
