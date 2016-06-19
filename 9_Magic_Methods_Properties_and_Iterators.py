#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
# 构造方法
以__metaclass__ = type 开始的是新式类
__init__方法
python 旧版本调用未绑定的超类的问题
调用超类 Unbound.__init__(self)


# 使用super 函数
super 函数只在新式类中起作用
super(Class, self).__init__()

'''

#__metaclass__ = type
#class Bird:
#	def __init__(self):
#		self.hungry = True
#
#	def eat(self):
#		if self.hungry:
#			print "Ahhh"
#			self.hungry =False
#
#		else:
#			print 'No thanks! '
#class SongBird(Bird):
#	def __init__(self):
#		super(SongBird, self).__init__()
#		self.sound = 'Squaek'
#	def sing(self):
#		print self.sound
#
#sb = SongBird()
#sb.sing()
#sb.eat()

###############################################################################

'''
# 面向对象的高级编程

## 使用__slots__ 限制class能添加的属性

对继承的子类没有作用

# property
@property 装饰器把方法变成属性调用

[参考链接](http://python.jobbole.com/80955/)


# 装饰器
通过变量能调用函数,装饰器是一个以另一个函数为参数的函数


装饰器：在代码运行期间动态增加功能的方式，本质上，decorator返回函数的一个高阶函数

[参考链接](http://www.wklken.me/posts/2013/07/19/python-translate-decorator.html)
'''
#'''
def My_decorator(fuction_of_decorator):
    def origin_function():
        print "我不是‘程序’"
        fuction_of_decorator()
        # 需要带括号
        print "‘程序’运行完了"
    return origin_function

def Stand_alone():
    print "这是独立的函数"

Stand_alone()

@My_decorator
def That_me():
    print "我是‘程序’"

That_me()
