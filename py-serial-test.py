import serial  # pyserial

try:
    portx = "COM6"
    bps = 57600
    timex = None

    ser = serial.Serial(portx, bps, timeout=timex)
    print("串口详情参数：", ser)


    def ReadOneByte():
        ByteRead = ser.read().hex()
        return ByteRead

    bb = ser.read().hex()
    print(type(bb))
    print(type(ser.read().hex()))

    a = 0
    while a < 30:
        if ReadOneByte() == 'aa':
            if ReadOneByte() == 'aa':
                # print(ReadOneByte()) 04-small
                if ReadOneByte() == '04':
                    # small packet
                    check1 = hex(int(ReadOneByte()))     # guess 0x80
                    print(type(check1))
                    check2 = ReadOneByte()          # guess 0x02
                    s_high = ReadOneByte()          # raw data HighBit
                    s_low = ReadOneByte()           # raw data LowBit
                    s_checksum = ReadOneByte()      # checksum to check
                    s_sum = ((check1 + check2 + s_high + s_low) ^ 0xFFFFFFFF) & 0xFF
                    print(s_sum == s_checksum)
                elif ReadOneByte() == '20':
                    pass
        a += 1

    # print(ReadOneByte())
    print("----------")
    ser.close()  # 关闭串口

except Exception as e:
    print("error!", e)