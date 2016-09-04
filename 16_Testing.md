# 测试

## 先测试，后编码

测试驱动开发

## 测试工具

### 文档测试

Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

### 单元测试

以test 开头的方法是测试方法，否则，不会在测试的时候执行

    import unittest

    from mydict import Dict

    class TestDict(unittest,TestCase):

        def test_init(self):
            d=Dict(a=1, b='test')
            self.assertEquals(d.a, 1)
            self.assertEquals(d.b, 'test')
            sele.assertTrue(isinstance(d, dict))

        def test_key(self):
            d = Dict()
            d['key'] = 'value'
            self.assertEquals(d.key, 'value')

        def test_attr(self):
            d = Dict()
            d.key = 'value'
            self.assertTrue('key' in d)
            self.assertEquals(d['key'], 'value')

        def test_keyerror(self):
            d = Dict()
            with self.assertRaises(KeyError):
            value = d[‘empty’]

        def test_attrerror(self):
            d = Dict()
            witj self.assertRaises(AttributError):
                value = d.empty

可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。                

## 单元测试以外的内容

### Pychecker 和PyLint

### 
