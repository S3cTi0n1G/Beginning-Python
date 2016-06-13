#!/usr/bin/python
# -*- coding: utf-8 -*-

from string import Template
s = Template('$x, good $x!')
s.substitute(x = 'bad')
#替换

print "prince of egg: %.2f" % 42
#f为浮点数

import math
math.pi
print "pi = %.2f" % math.pi
#保留两位小数

print "pi = %10f" % math.pi
#width = 10

print "pi = %010f" % math.pi
#前面补０

print "pi = %010.5f" % math.pi
#保留５为小数，前面补０

print "pi = %*.*f" % (20, 10, math.pi)
#使用×替代宽度和小数位

print "pi = %+2f" % math.pi
#用＋显示正负号

print "pi = %-10.2f" % math.pi
#用－表示左对齐

print ('% 5d' % 10) + '\n' + ('%5d' % -10)
#空白‘’表示在正数前增加一个空格

print "＃问题：怎么在小数点s后面补零？＃"

s = 'Lucy in the sky with dimond'
print s.find('sky')
#find,找到字符串中的子串位置，未找到返回－１

'''本章节的其他string method :
link.join(seq),用link连接字符串seq；
str.lower()表示转换str内的字母为小写；
str.title(),转换str内的首字母大写，建议用string.capwords(str)；
seq.replace('words')查找替换seq中的words；
seq.split('symbol')以symbol为分隔符分开seq；
seq.strip('symbol')去除seq前后指定的symbol，symbol为空者去掉字符串两端的空格;
maketrans 字符替换　

 
