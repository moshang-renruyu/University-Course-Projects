"""
Python 模块(Module)，是一个 Python 文件，以 .py 结尾.  模块能定义函数，类和变量，模块里也能包含可执行的代码.

模块的作用:  python中有很多各种不同的模块, 每一个模块都可以帮助我
们快速的实现一些功能, 比如实现和时间相关的功能就可以使用time模块
我们可以认为一个模块就是一个工具包, 每一个工具包中都有各种不同的
工具供我们使用进而实现各种不同的功能.


大白话：模块就是一个Python文件，里面有类、函数、变量等，我们可以
拿过来用（导入模块去使用）

"""

"""
模块在使用前需要先导入 导入的语法如下:
[from模块名］import［模块丨类丨变量丨函数丨*］[as别名]
常用的组合形式如：
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名

注意事项：
from可以省略，直接import即可
as别名可以省略
通过”.”来确定层级关系
模块的导入一般写在代码文件的开头位置
"""
# import time
# print("薛锐")
# time.sleep(3)
#
# print("上班")

# from time import sleep
# print("Hello")
# sleep(2)
# print("d")


from time import *
print("Hello")
sleep(2)
print("d")

import  time as t
print("Hello")
t.sleep(2)
print("d")

from time import sleep as s
print("Hello")
s(2)
print("d")
