"""
None类型
思考：如果函数没有使用return语句返回数据，那么函数有返回值吗？

实际上是：有的。

Python中有一个特殊的字面量：None，其类型是：<class 'NoneType'>
无返回值的函数，实际上就是返回了：None这个字面量

None表示：空的、无实际意义的意思
函数返回的None，就表示，这个函数没有返回什么有意义的内容。
也就是返回了空的意思
None类型的应用场景
None作为一个特殊的字面量，用于表示：空、无意义，其有非常多的应用场景。
用在函数无返回值上

用在if判断上
在if判断中，None等同于False
一般用于在函数中主动返回None，配合if判断做相关处理

用于声明无内容的变量上
定义变量，但暂时不需要变量有具体值，可以用None来代替

函数如何返回None
不使用return语句即返回None
主动return None

"""
def hi():
    print("hi")
result=hi()
print(result)
print(type(result))

def hi2():
    print("hi2")
    return None
result=hi2()
print(result)
print(type(result))

def check_age(age):
    if age > 18:
         return "sUccEss"
    return None
result = check_age(20)
if not result:
     print("未成年，不可进入")

