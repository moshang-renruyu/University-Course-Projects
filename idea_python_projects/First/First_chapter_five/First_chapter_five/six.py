"""
1. 什么是函数返回值？
函数在执行完成后，返回给调用者的结果
2. 返回值的应用语法：
使用关键字：return 来返回结果
3. 注意：
函数体在遇到return后就结束了，所以写在return后的代码不会执行。

def函数（参数．）：
   函数体
   return返回值
变量 = 函数(参数)
如上，变量就能接收到函数的返回值
语法就是：通过return关键字，就能向调用者返回数据

"""
def add(a,b):
    result=a+b
    return result
r=add(5,6)
print(r)