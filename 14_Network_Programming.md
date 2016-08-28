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
