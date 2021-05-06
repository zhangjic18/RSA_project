import random
import sys

from gcd import gcd
from inverse_element import inverse_element
from large_prime_number import large_prime_number
from mod_exp import mod_exp
from get_m import get_m
from get_string import get_string

sys.setrecursionlimit(100000)  # 例如这里设置为100000

p = large_prime_number()  # 生成生成两个大素数 p 和 q
q = large_prime_number()
while p == q:
    q = large_prime_number()

n = p * q  # 计算n
φ_n = (p - 1) * (q - 1)  # 计算φ_n

e = random.randint(2, φ_n - 1)  # 计算e
while gcd(e, φ_n) != 1:
    e = random.randint(2, φ_n - 1)

d = inverse_element(e, φ_n)  # 计算d

m = get_m("I love you")  # 明文->数字

c = mod_exp(m, e, n)  # 加密
m_decoded = mod_exp(c, d, n)  # 解密
string_decoded = get_string(m_decoded)  # 数字->明文

print("明文：", "I love you")
print("明文对应的数字:", m)
print("密文：", c)
print("通过密文解密得到的数字:", m_decoded)
print("通过密文解密得到的数字对应的字符串:", string_decoded)

import os
print("\n".join(os.listdir(os.getcwd())))
