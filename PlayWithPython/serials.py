import serial  # pyserial


def str2hex(data):
    # only for 1 bit data
    data_sum = 0
    for i in {0, 1}:
        if data[i] not in {'a', 'b', 'c', 'd', 'e', 'f'}:
            data_sum += pow(16, 1-i) * int(data[i])
        elif data[i] == 'a':
            data_sum += pow(16, 1-i) * 10
        elif data[i] == 'b':
            data_sum += pow(16, 1-i) * 11
        elif data[i] == 'c':
            data_sum += pow(16, 1-i) * 12
        elif data[i] == 'd':
            data_sum += pow(16, 1-i) * 13
        elif data[i] == 'e':
            data_sum += pow(16, 1-i) * 14
        elif data[i] == 'f':
            data_sum += pow(16, 1-i) * 15
    return data_sum
    # print(data_sum)
    # print(hex(data_sum))


def ReadOneByte():
    ByteRead = ser.read().hex()
    return ByteRead


try:
    portx = "COM6"
    bps = 57600
    timex = None

    ser = serial.Serial(portx, bps, timeout=timex)
    print("串口详情参数：", ser)

    #print(ReadOneByte()==170)
    n = 0
    a = 0
    while 1:
        n += 1
        if str2hex(ReadOneByte()) == 0xAA:
            # print("hello")
            if str2hex(ReadOneByte()) == 0xAA:
                # print("hello")
                if str2hex(ReadOneByte()) == 0x04:
                    #print("hello")
                    # small packet
                    check1 = str2hex(ReadOneByte())          # guess 0x80
                    check2 = str2hex(ReadOneByte())          # guess 0x02
                    s_high = str2hex(ReadOneByte())          # raw data HighBit
                    s_low = str2hex(ReadOneByte())           # raw data LowBit
                    s_checksum = str2hex(ReadOneByte())      # checksum to check
                    #print("hello")
                    # print(check1 + check2 + s_high + s_low)
                    # print(s_checksum)
                    # print(~(check1 + check2 + s_high + s_low))
                    # print(~(check1 + check2 + s_high + s_low) & 255)
                    # print("---------------")
                    s_sum = ~(check1 + check2 + s_high + s_low) & 255   # FFFFFFFF = 4294967295     FF = 255
                    if s_sum == s_checksum:
                        a += 1
                        # print("丢包率内: ", (n - a) / n)    # 内层丢包率的计算
                        if ((n - a) / n) < 0.10:
                            rawdata = (s_high << 8) | s_low
                            if(rawdata > 32768):
                                rawdata -= 65536
                            print(rawdata)

                elif ReadOneByte() == 0x20:
                    pass

        # print("丢包率外: ", (n-a)/n)  # 外层丢包率的计算

    # print(ReadOneByte())
    print("----------")
    ser.close()  # 关闭串口

except Exception as e:
    print("error!", e)
