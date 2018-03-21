# Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('包含中文的str')
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
# 如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587')
# Python对bytes类型的数据用带b前缀的单引号或双引号表示.
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# 因为中文编码的范围超过了ASCII编码的范围，Python会报错。
x = b'ABC'
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))
# 我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 要计算str包含多少个字符，可以用len()函数
print(len('ABC'))
print(len('中文'))
# 如果换成bytes，len()函数就计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
