#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
# 构造方法
以__metaclass__ = type 开始的是新式类
__init__方法
python 旧版本调用未绑定的超类的问题

# 使用super 函数
super 函数只在新式类中起作用

''' 

#__metaclass__ = type
#class Bird:
#    def __init__(self):
#        self.hungry = True
#    
#    def eat(self):
#        if self.hungry:
#            print "Ahhh"
#            self.hungry =False
#            
#        else:
#            print 'No thanks! '
#class SongBird(Bird):
#    def __init__(self):
#        super(SongBird, self).__init__()
#        self.sound = 'Squaek'
#    def sing(self):
#        print self.sound
#        
#sb = SongBird()
#sb.sing()
#sb.eat()

###############################################################################

'''
# 面向对象的高级编程

## 使用__slots__ 限制class能添加的属性

# property 
@property 装饰器把方法变成属性调用

## 装饰器







