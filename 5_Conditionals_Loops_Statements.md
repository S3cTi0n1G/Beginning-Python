# print
使用逗号输出
>print 'Age:',42

*使用　**,**　使得无间隔输出*

#import
import 为别名
>import math as rule   

#赋值
多个赋值
>x, y, z = 1, 2, 3

交换变量
>x, y = y, x

链式赋值
>x = y = somefunction() 

#条件和语句
以下会被作为　**false**

False None 0 "" () [] {}
*其他一切都被解释为真（ture）*

##条件执行和if
if

else

elif

##比较运算符
相等运算
> 'foo' == 'foo'

**is** 同一性比较
is　比较同一性而非相等性，is 用于判断两者是否等同（同一对象）

**in**　成员资格运算符
>same = 'sandstorm'
>'s' in same
>Ture

字符串和序列比较
> 'alpha' > 'beta'

布尔运算符
and
or
not

#if的断言
assert的用法：在条件后添加

#loop
## while loop
## for loop
用for 遍历列表

*能用for循环，尽量不用while循环*

##一些迭代工具
1. 并行迭代
    zip函数，用来并行迭代，压缩多个序列为一个元组。
    *压缩不等长的序列时，到最短的序列用完时即止。*
2. 按索引迭代
3. 翻转和排序迭代
    
    reversed
    
    sorted
    
##跳出循环
break

continue

while True:
    break   
    
**避免频繁使用break影响代码可读性**

#列表推导式
列表推导式是利用其他列表创建新列表的一种方法
> [x*x for x in range(10) if x % 2 ==0]

##del用来删除变量或数据结构的一部分

##使用exec和eval执行和求值字符串
**HOW**







