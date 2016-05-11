#!/usr/bin/python
# -*- coding: utf-8 -*-

age = {'adam':'10','bell':'20','cindy':30,'dustin':'40','elsa':'50'}
print "dustin's age is %(dustin)s." % age
#字典的格式化字符串

'''
# 字典的method
    >>>dict = {}
字典的清除，可清除关联字典的键和键值
    >>>returned_value = dict.clear()
    >>>d
    {}

字典的复制
x = {}
y= x.copy
复制后，替换y的值，x不受影响；修改y的值，x同样受影响。

深复制
    >>>from copy import deepcopy
    >>>d = {}
    >>>dc = deepcopy(d)
    
fromkeys使用给定的键建立新的字典,使用unkown作为默认值，可以不指定默认值。
    >>>dict.fromkeys(['name', 'age'].'unkown')
    
用dict.get('value')访问字典中的键， 并返回键值。

dict.items() 返回以列表形式返回乱序的键和键值

其他method
    dict.keys() 返回键
    dict.pop('keys')　和dict.popitems() 随机删除
    dict.setdefault('keys','value') 键keys不存在时，创建并设置keys的默认值为value
    dict.update(x) 用x更新dict
    dict.values() 用列表的形式返回键值
'''


