"""
1. 函数本身是可以作为参数，传入另一个函数中进行使用的。
2. 将函数传入的作用在于：传入计算逻辑，而非传入数据。
"""
def com (add):
    result=add(1,3)
    print(type(add))
    print(result)
def add(x,y):
    return x+y
com(add)