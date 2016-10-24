# 笔记

一个进程至少有一个线程

多任务实现的3种方式：

    多进程

    多线程

    多进程+多线程

# 多进程

Windows没有fork调用，mutliprocessing 是跨平台版的多进程模块

## multiprocessing
	from multiprocessing import Process
	import os
	
	def run_proc(name):
	    print 'Run child process %s (%s)...' % (name, os.getpid())
	#定义执行函数	
	if __name__ == '__main__':
	    print 'Parent process %s.' % os.getpid()
	    p = Process(target=run_proc, args=('test',))
        #创建实例
	    print 'Process will start'
	    p.start()
        #运行
	    p.join()
        #等待子进程结束后往下运行
	    print 'Process end.'

## Pool

用于批量创建子进程，默认创建的数量由系统CPU 核心数决定

## 进程间的通信

# 线程

两个线程的模块:thread、threading，少使用前者

## Lock

锁住线程，按步执行

# ThreadLocal

Pending...

# 多进程、多线程比较

多进程稳定性高，当耗资源。

多线程比多进程略快，各线程共享进程内存。

I/O 密集型的Python 程序要比计算密集型的代码能够更好地利用多线程

# 分布式进程

Pending...
