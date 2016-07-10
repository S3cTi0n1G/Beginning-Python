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

q.rotate(n)
deque中的元素向右移动n个位置。如果n是负数的向左移动

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

  子模式使用括号 p(ython|erl)

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
