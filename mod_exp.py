def mod_exp(a, b, c):  # a ^ b % c
    result = 1
    a %= c
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        b //= 2
        a = a ** 2 % c
    return result
