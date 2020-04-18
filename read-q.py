import time
import serial

ser = serial.Serial(
    port='COM6',
    baudrate=57600,
    parity=serial.PARITY_ODD,  # 校验位 
    stopbits=serial.STOPBITS_TWO,  # 停止位
    bytesize=serial.SEVENBITS  # 数据位
)
data = ''

while True:
    data = ser.readline()
    # t = time.time()
    # ct = time.ctime(t)
    # print(ct, ':')
    print(data)

    # f = open('D:/test.txt', 'a')
    # f.writelines(ct)
    # f.writelines(':\n')
    # # f.writelines(data.decode('utf-8'))
    # f.writelines(str(data))
    # f.close()