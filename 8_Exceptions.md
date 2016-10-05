# try: / except: / finally: 处理机制

    try:
        print 'try...'
        r = 10 / 5
        print 'rusult:', r
    except ZeroDivisionError,e:
        print 'except：', e
    finally:
        print 'finally...'
    print 'END'

# 调试

断言 assert
增加一个条件，为真就什么都不做

    def foo(s):
        n = int(s)
        assert n != 0, 'n is zero!'
        return 10 / n

assert的意思是，表达式n != 0应该是True，否则，后面的代码就会出错。

启动python 解释器可以用-0 参数来关闭assert

# logging

    Import logging
    loggong.basicConfig(level=logging.INFO)

打印错误记录,level有debug，info，warning，error等几个级别

# pbd调试工具

让程序以单步方式运行

pdb.set_trace()

n = input('>>>')
def foo(n):
    assert n != 0, 'Zero Error'
    return n / 1
foo(n)
