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
