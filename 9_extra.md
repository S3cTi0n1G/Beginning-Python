# 第九章补充知识点

## 迭代器

___iter___方法返回一个迭代器

    class Fibs:
        def ___init___(self):
            self.a = 0
            self.b = 1
        def next(self):
            self.a, self.b = self.b, self.a + self.b
            return self.a
    def ___init___(self):
        return self

# 生成器（generator）
## 生成器推导式
把列表生成式的[]改成()，可以创建generator
    >>>L = [x for x in range(10,20,2)]
    # 列表生成式
    >>>g = (x for x in range(10,20,2))
    # 生成器

使用for 循环打印生成器    

## yield 语句


# 递归

# 安装了Atom git 配置完毕，可以开始了。

# 准备开个git 博客吧，正好有个教程可以发表了
