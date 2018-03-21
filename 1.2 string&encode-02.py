#!/usr/bin/env python3   第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# -*- coding: utf-8 -*-   第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你中文输出可能会有乱码
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# 练习:小明的成绩从去年的72分提升到了今年的85分，计算提升的百分点，用字符串格式化显示出'xx.x%'，只保留小数点后1位
# -*- coding: utf-8 -*-
s1 = 72
s2 = 85
r = (s2 - s1) / s1
print('%.1f%%' % (r * 100))
