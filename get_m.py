def get_m(string):
    # string不超过200个字符
    # 双方约定utf-8
    string_ = string.encode("utf-8")
    string_list = [bin(int(i))[2:].rjust(8, '0') for i in string_]
    string_bit = ''.join(string_list)
    return int(string_bit, 2)
