## socket 模块

### socket 实例化需要三个参数

socket.socket(socket.AF_INET, socket.SOCK_STEAM, )

    第一个参数，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。
    第二个参数，SOCK_STREAM 指定使用面向流的TCP协议；SOCK_DGRAM 数据报式使用UDP
    第三个参数，默认0，不需要提供

一个服务端代码

    import socket

    s = socket.socket()

    host = socket.gethostname()
    # gethostname 函数获取当前主机名称
    port = 1234
    # linux 系统中，需要admin 权限才能使用1024 以下的port
    s.bind((host, port))

    s.listen(5)
    # 操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
    while True:
        c, addr = s.accept()
        print ‘Got Connection from’, addr
        s.send('Thank you for Connecting')
        c.close()

## urllib 和 urllib2 模块

### 区别

* urllib2 可以接受一个 Request 对象，并以此可以来设置一个 URL 的 headers，但是 urllib 只接收一个 URL。这意味着，你不能伪装你的用户代理字符串等。
* urllib 模块可以提供进行 urlencode 的方法，该方法用于 GET 查询字符串的生成，urllib2 的不具有这样的功能。这就是 urllib 与 urllib2 经常在一起使用的原因。

[扩展阅读][1]

### 打开远程文件（Read-Only）

    from urllib import urlopen
    webpage = urlopen('http://www.python.org')
    # 打开网页
    file_open = urlopen('file:///home/section/tmp/aa.log')
    # 打开文件,注意对 \ 转义

urlopen 返回的类文件对象支持close、read、readline、readlines 方法

### 获取远程文件

urlretrieve 返回一个元组(filename, headers)

## SocketServer

？？？

## 多个连接

forking threading 异步I/O

### Twisted

pass

-----------------
[1]: http://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html "外部链接"  
