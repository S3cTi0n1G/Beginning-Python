# 模块
模块只能导入一次

为了能让代码可重用，可以模块化

## 条件测试代码
>def test():
>   print "test"
>if __name__ =' __main__' :test()

## 导入为别名

## 包
按目录来组织模块的方法，称为包

每一个包目录下面必须有一个__init__.py的文件

# 探究模块
## 使用dir 查看模块中的内容

## __all__ 变量
设置__all__ 变量过滤不需要的的变量、函数、类

## 用help 获取帮助

# 标准库
## 集合
frozenset 构造函数创建给定集合的副本

## 堆
堆属性：位于i 位置上的元素种比i/2 位置处的元素大
> from heapq omport *

heapify 函数使用任意列表作为参数，并将其转换为合法的堆

## 双端序列

> from collections import deque

deque 实现了list 的append()和pop()，还支持appendleft()和popleeft()

q.rotate(n)，deque中的元素向右移动n个位置。如果n是负数的向左移动

## time

>time.asctime(tuple)

将9个元素的数组转换为时间形式的字符串

>time.sleep(secs)

休眠secs 秒

>time.mktime(tuple)

把tuple 转换为本地时间（秒数）

>time.time()

当前秒数，新纪元开始的秒数，以UTC为准

>time.localtime(secs)
将secs 秒转换为日期元组，以本地时间为准

## 随机数
>from random import *

>random()

返回0<n<=1 之间的随机实数n

>getrandbits(n)

 返回长度为n位的长整型随机数

> uniform(a, b)

返回随机实数n,其中a<= n <b

>randrang(start, stop, step)

返回range(start, stop, step) 中的随机数

>seq = 'abcdefg12345'
>choice(seq)
>'1'

返回序列seq 中随意元素

>sample(seq, n)

返回序列seq 中n 个随机且不重复的元素

## re
re 模块包含了对正则表达式 *（regular expression）* 的支持

[参考资料](http://www.runoob.com/python/python-reg-expressions.html)


* 通配符 *wildcard*

  . 可以匹配一个字母

* 对通配符转义

  python\\.org 匹配 python.org

  或： r'python\.org'

* 字符集

  [az]ython 匹配a或z

  [a-z]ython 按字母顺序匹配a-Z

  [a-zA-Z0-9]能够匹配任意大小写字母和数字

  字符集只能匹配一个这样的字符

  [^a-z] 反转字符集

* 选择符和子模式

  使用管道符号 |

  子模式使用括号 p(ython|erl),表示匹配python  或perl

* 可选项

  在子模式后面加上问号

  问号表示子模式可以出现一次或不出现

* 重复多次

  a* 允许a 重复0次或多次

  a+ 允许a 重复1次或多次

  a{m,n} 允许模式重复m~n 次

* 字符串的开始和结尾

  ^ 只在开头匹配

  $ 只在末尾匹配

## re 模块

* re.compile(pattern[, flags])

把正则表达式的模式和标识转化成正则表达式对象，供 match() 和 search() 这两个函数使用。

* re.match() 在给定字符串开头匹配

* re.search() 在给定的字符串中寻找第一个匹配的子字符串

* re.split(pattern, 'some_thing') 根据pattern 分割

  如果pattern 中包括括号，括起来的字符会散布在子字符串之间

  some_thing 后面接maxsplit=n 参数,表示最多分割n 次

*  re.sub(pat, repl, string, count=0, flags=0) 将string  中匹配pat 的内容替换为repl,可选参数 count 是模式匹配後替换的最大次数；count 必须是非负整数。缺省值是 0 表示替换所有的匹配。如果无匹配，字符串将会无改变地返回。

*  re.escape() 将字符串转换为正则表达式能识别的部分

* flags=0 参数的用法

re.I 忽略大小写

re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境

re.M 多行模式

re.S 即为’ . ’并且包括换行符在内的任意字符（’ . ’不包括换行符）

re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库

re.X 为了增加可读性，忽略空格和’ # ’后面的注释,即啰嗦模式

## 匹配对象和组

re 模块同时返回了哪个模块匹配了哪些信息

组的方法：group start end span

## 作为替代的组号和函数

* 贪婪和非贪婪模式

在重复运算符后加 +

例如 +?,表示尽可能少的匹配

# 更多自带模块

## collections

nametuple，用于创建一个自定义的tuple 对象

defaultdict，一种在引用不存在的值时，返回一个默认值的dict。

OrderedDict，实现按key的插入顺序排列的dict

Counter，一个简单的计数器，可统计字符出现的个数。

## base64

base64，是一种用64个字符来表示任意二进制数据的方法

>>>import base64

>>>base64.b64encode('txture') 

>>>base64.b64decode('txture')

base64 编码后会把=去掉，解码需要加上，Base64编码的长度永远是4的倍数。

## struct

Python 提供了一个struct模块来解决str和其他二进制数据类型的转换

## hashlib

hahlib 提供了常见的摘要算法，如MD5，SHA1等

    import hashlib
    
    md5 = hashlib.md5()
    md5.update('hind this')
    print md5.hexdigest()

## itertools

用于操作迭代对象的函数

itertools.count() 创建一个无限的迭代器

itertools.cycle() 把传入的一个序列无限重复下去 

itertools.repeat() 负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数

通过itertools.takewhile()等函数根据条件判断来截取出一个有限的序列

itertools.chain() 把一组迭代对象串联起来

itertools.groupby()把迭代器中相邻的重复元素挑出来放在一起

itertools.imap() 可以作用于无穷序列，返回迭代对象，而map()返回list

## XML

## HTMLParser

