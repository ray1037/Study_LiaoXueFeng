# 整数
print(3)
# 浮点数
print(3.1)
# 字符串
print('I\'m \"OK\"!')
print("I'm learning\nPython.")
print("\\\n\\")
# Python还允许用r''表示''内部的字符串默认不转义，可以自己试试
print('\\\t\\')
print(r'\\\t\\')
# Python允许用'''...'''的格式表示多行内容，可以自己试试：
print('''line1
line2
line3''')
print(r'''hello,\n
world''')
# 布尔值
# 变量
a = 'ABC'
b = a
a = 'XYZ'
print(b)
# 常量运算
print(10 / 3)
print(9 / 3)
print(10 // 3)
print(10 % 3)
# 练习
# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n, '\n', f, '\n', s1, '\n', s2, '\n', s3, '\n', s4)
