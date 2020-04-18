
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


a = '04'
print(type(str2hex(a)))
print(str2hex(a))
print(str2hex(a) == 0x04)
