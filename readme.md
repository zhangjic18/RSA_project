​	运行demo.py即可得到明文为"I love you"时的加解密结果。

# 1 文件目录如下所示：

```python
.idea
demo.py
gcd.py
get_m.py
get_string.py
inverse_element.py
large_prime_number.py
mod_exp.py
readme.md
__pycache__
```

# 2 各文件及其内部函数说明如下：

gcd.py：

​	def gcd(x, y)：求x和y的最大公约数

get_m.py

​	def get_m(string)：将字符串string按照ASCII码编码为数字

get_string.py：

def get_string(num_received)：将解密得到的数字num_received按照ASCII码解码成字符串

inverse_element.py：

​	def inverse_element(e, $φ\_n$)：计算e在mod $φ\_n$意义下的逆元素

large_prime_number.py：

​	def large_prime_number()：通过Miller-Rabin素数测试算法生成1024 bit的大素数

mod_exp.py：

​	def mod_exp(a, b, c)：快速模幂算法，快速计算$a ^ b \% c$
