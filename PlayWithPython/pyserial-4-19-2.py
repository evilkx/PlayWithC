import serial  # pyserial


def hexstr2int(data):
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
    portx = "COM10"
    bps = 57600
    timex = None

    ser = serial.Serial(portx, bps, timeout=timex)
    print("串口详情参数：", ser)

    #print(ReadOneByte()==170)
    n = 0
    a = 0
    while 1:
        n += 1

        if hexstr2int(ReadOneByte()) == 0xAA:
            # print("hello")
            if hexstr2int(ReadOneByte()) == 0xAA:
                # print("hello")
                temp = hexstr2int(ReadOneByte())
                if temp == 0x04:
                    #print("hello")
                    # small packet
                    check1 = hexstr2int(ReadOneByte())          # guess 0x80
                    check2 = hexstr2int(ReadOneByte())          # guess 0x02
                    s_high = hexstr2int(ReadOneByte())          # raw data HighBit
                    s_low = hexstr2int(ReadOneByte())           # raw data LowBit
                    s_checksum = hexstr2int(ReadOneByte())      # checksum to check

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

                elif temp == 0x20:
                    # print("hello222")
                    if hexstr2int(ReadOneByte()) == 0x02:
                        sig = hexstr2int(ReadOneByte())
                        if hexstr2int(ReadOneByte()) == 0x83:
                            if hexstr2int(ReadOneByte()) == 0x18:
                                print("Here is EEG data")
                                delta_h = hexstr2int(ReadOneByte())
                                delta_m = hexstr2int(ReadOneByte())
                                delta_l = hexstr2int(ReadOneByte())
                                theta_h = hexstr2int(ReadOneByte())
                                theta_m = hexstr2int(ReadOneByte())
                                theta_l = hexstr2int(ReadOneByte())

                                l_alpha_l = hexstr2int(ReadOneByte())
                                l_alpha_m = hexstr2int(ReadOneByte())
                                l_alpha_h = hexstr2int(ReadOneByte())
                                h_alpha_l = hexstr2int(ReadOneByte())
                                h_alpha_m = hexstr2int(ReadOneByte())
                                h_alpha_h = hexstr2int(ReadOneByte())

                                l_beta_l = hexstr2int(ReadOneByte())
                                l_beta_m = hexstr2int(ReadOneByte())
                                l_beta_h = hexstr2int(ReadOneByte())
                                h_beta_l = hexstr2int(ReadOneByte())
                                h_beta_m = hexstr2int(ReadOneByte())
                                h_beta_h = hexstr2int(ReadOneByte())

                                l_gamma_l = hexstr2int(ReadOneByte())
                                l_gamma_m = hexstr2int(ReadOneByte())
                                l_gamma_h = hexstr2int(ReadOneByte())
                                m_gamma_l = hexstr2int(ReadOneByte())
                                m_gamma_m = hexstr2int(ReadOneByte())
                                m_gamma_h = hexstr2int(ReadOneByte())

                                if hexstr2int(ReadOneByte()) == 0x04:
                                    attention = hexstr2int(ReadOneByte())       # attention 0-100
                                    if hexstr2int(ReadOneByte()) == 0x05:
                                        meditation = hexstr2int(ReadOneByte())  # meditation 0-100
                                        b_checksum = hexstr2int(ReadOneByte())  # big packet checksum
                                        print("专注度：", attention)
                                        print("放松度：", meditation)

                                        delta = delta_h << 16 | delta_m << 8 | delta_l
                                        theta = theta_h << 16 | theta_m << 8 | theta_l

                                        l_alpha = l_alpha_h << 16 | l_alpha_m << 8 | l_alpha_l
                                        h_alpha = h_alpha_h << 16 | h_alpha_m << 8 | h_alpha_l
                                        alpha = h_alpha << 24 | l_alpha

                                        l_beta = l_beta_h << 16 | l_beta_m << 8 | l_beta_l
                                        h_beta = h_beta_h << 16 | h_beta_m << 8 | h_beta_l
                                        beta = h_beta << 24 | l_beta

                                        m_gamma = m_gamma_h << 16 | m_gamma_m << 8 << m_gamma_l
                                        l_gamma = l_gamma_h << 16 | l_gamma_m << 8 << l_gamma_l
                                        gamma = m_gamma << 24 | l_gamma

                                        print("delta: ", delta)
                                        print("theta: ", theta)
                                        print("alpha: ", alpha)
                                        print("beta: ", beta)
                                        print("gamma: ", gamma)

        # print("丢包率外: ", (n-a)/n)  # 外层丢包率的计算

    # print(ReadOneByte())
    print("----------")
    ser.close()  # 关闭串口

except Exception as e:
    print("error!", e)
