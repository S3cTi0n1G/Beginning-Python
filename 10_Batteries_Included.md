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

## 双堆序列
> from collections import deque
