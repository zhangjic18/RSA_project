def gcd(x, y):
    if x > y:
        if x % y == 0:
            return y
        else:
            return gcd(x % y, y)
    elif x < y:
        if y % x == 0:
            return x
        else:
            return gcd(x, y % x)
    else:
        return x
