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
'''
def my_shiny_new_decorator(a_function_to_decorate):

    # 在这里，装饰器定义一个函数： 包装器.
    # 这个函数将原始函数进行包装，以达到在原始函数之前、之后执行代码的目的
    def the_wrapper_around_the_original_function():

        # 将你要在原始函数之前执行的代码放到这里
        print "Before the function runs"

        # 调用原始函数(需要带括号)
        a_function_to_decorate()

        # 将你要在原始函数之后执行的代码放到这里
        print "After the function runs"

    # 代码到这里，函数‘a_function_to_decorate’还没有被执行
    # 我们将返回刚才创建的这个包装函数
    # 这个函数包含原始函数及要执行的附加代码，并且可以被使用
    return the_wrapper_around_the_original_function

# 创建一个函数
def a_stand_alone_function():
    print "I am a stand alone function, don't you dare modify me"

a_stand_alone_function()
#outputs: I am a stand alone function, don't you dare modify me

# 好了，在这里你可以装饰这个函数，扩展其行为
# 将函数传递给装饰器，装饰器将动态地将其包装在任何你想执行的代码中，然后返回一个新的函数
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)

# 调用新函数，可以看到装饰器的效果
a_stand_alone_function_decorated()
#outputs:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the function runs
'''
