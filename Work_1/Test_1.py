# Author: ZhangBo
# CreatTime:2022/10/5
# Email:1713659406@qq.com
# print(2 + 5)
ddd = """
字符串
可换行
随意换
"""  # “”“...”“”为多行输入
# print(ddd)
# print("我是\"傻逼\"")  # \取消转义
# 注释 ，不会运行
abc = "sda" \
      "s"
# print(abc)
# print(2 // 4)  # =0，0.5向下取整
# print(7 % 3)  # =1，取余 7➗3=2.....1
# print(2 ** 3)  # =8，幂运算
name = "小仙女长相甜美并且温柔"
# print(name[:-1])  # 开始=0，结尾=-1，[开始:结尾:步长]取左不取右;从左往右写 -->> [-3:-1]√；[-1:-3]×
a = "我的名字叫{},{}"
# print(a.format("zb", "18岁"))
a = "我%.2f你" % 99.98456  # 保留2位小数写法->> .2f
# print(a)
# insert 插入  del 删除  append 增加
b = ["world", "hello", "python", "hello"]
# b.remove("hello") 移除第一个“hello”
# b.pop(2) 移除索引值为2的参数
# print(b)
b1 = b.index('hello')  # 得到第一个hello的索引值
# print(b1)
