def get_string(num_received):
    # 双方约定utf-8
    num_received_bin = bin(num_received)[2:]
    while len(num_received_bin) % 8 != 0:
        num_received_bin = "0" + num_received_bin

    list_1 = []
    for i in range(1, len(num_received_bin) // 8 + 1):
        list_1.append(''.join(num_received_bin[(i - 1) * 8:i * 8]))

    list_2 = []
    for i in list_1:
        list_2.append(chr(int('0b' + i, 2)))

    string_received = ''.join(list_2)
    return string_received
