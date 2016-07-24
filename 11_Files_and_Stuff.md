# 文件和流

## 打开文件

>f = open(name[, mode[,buffering]])

mode 和buffering 参数可选

## 模式

读模式

> f =open(filename, 'r')

写模式

> f =open(filename, 'w')

追加模式(只能写在末尾)

> f =open(filename, 'a')

二进制模式

> f =open(filename, 'rb')

*为什么使用二进制模式*

避免跨平台文件转换问题

读写模式

> f =open(filename, '+')

## 缓存

参数 0 无缓存，直接读取硬盘

参数 1 有缓存，缓存在内存，只有使用了flush 和close才会更新硬盘数据。大于1的数字大u币奥缓存大
小，-1 代表使用默认大小
