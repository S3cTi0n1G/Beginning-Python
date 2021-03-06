# 文件和流

## 打开文件

>>>f=open(name[, mode[,buffering]])

mode 和buffering 参数可选

## 模式

读模式

>>>f=open(filename, 'r')

写模式

>>>f=open(filename, 'w')

追加模式(只能写在末尾)

>>>f=open(filename, 'a')

二进制模式

>>>f=open(filename, 'rb')

*为什么使用二进制模式*

避免跨平台文件转换问题

读写模式

>>>f=open(filename, '+')

## 缓存

参数 0 无缓存，直接读取硬盘

参数 1 有缓存，缓存在内存，只有使用了flush 和close才会更新硬盘数据。大于1的数字大u币奥缓存大
小，-1 代表使用默认大小

## 使用With 语句

    with open('path/file', 'r') as f:
       print f.read()

# 字符编码

>>>u = f.read().decode('gbk')
以GBK 编码读取文件

使用codecs 模块自动转换编码

    import codecs
    with codecs.open('/path/test.txt', 'r', 'gbk') as f:
        f.read() # u'\u6d4b\u8bd5'

写入特定编码的文件方法类似

## 基本的文件方法

>f.write('string')

把字符串string 写入到文件最后

>f.read(size)

size 表示每次最多读取size个字节的内容，不写则默认读取全部

读取文件

### 三种标准流

stdin，stdout 以及 stderr 都是类文件对象，该对象实现了 UNIX 标准的 I/O 机制 (Windows 中也能使用)。

## 管式输出

管道符号（|）把一个命令的标准输出和下一个命令的输入连在一起

## 随机访问

>f.seek(offset, whence)

offset 指位置，whence 可选，默认0, 表示从文件头开始计算

>f.tell()

返回当前文件的位置

## 读写行

>readline()

>writeline()

>readlines()

readlines 打印所有行，返回一个列表

## 关闭文件

>file.close()

* 使用try/finally 语句关闭

* 使用with 语句
  >with open('/tmp/foo.txt') as somefile:
    date = file.read()

## 上下文管理器

参考

http://blog.jobbole.com/64175/

http://blog.jobbole.com/64175/

## 对文件内容迭代处理

* 按字节循环

'''

    f = open(filename)
    char = f.read()
    while char:
        process(char)
        char = f.read(1)
    f.close()
'''

* 按行操作

'''

    f = open(filename)
    while Ture:
        line = f.readline()
        if not line:break
        process(line)
    f.close()
'''

## 文件迭代器

文件对象是可迭代的，意味着可以在for 循环中使用它们

# 操作文件和目录

os 模块和os.path 模块

os.path.join() 合成路径

os.path.split() 拆分路径
    
    >>>os.path.split('/usr/lib/python2.7/posixpath.pyc')
    ('/usr/lib/python2.7', 'posixpath.pyc')

os.rename('test.py', 'test.md') 重命名文件

os.remove('file.py') 删除文件

os 模块不存在复制函数，可以从shutil 导入copyfile() 函数

# 序列化

序列化：把变量存储或传输的过程

##　pickle 模块

pickle.dump() 写入

pickle.load() 读取

## JSON 模块

读取写入的方法同上

Python的dict对象可以直接序列化为JSON的{}，其他的对象和类需要用函数转换



