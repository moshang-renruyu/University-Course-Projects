"""
异常捕获
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""
try:
    f=open("D:/abc.txt","r",encoding="UTF-8")
except:
    print("出现异常，改为w模式")
    f = open("D:/abc.txt", "w", encoding="UTF-8")
"""
捕获指定异常
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')
注意：
① 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
② 一般try下方只放一行尝试执行的代码。
"""

"""
捕获多个异常
当捕获多个异常时，可以把要捕获的异常类型的名字，放到except 后，并使用元组的方式进行书写。
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print('ZeroDivision错误...')
"""

"""
捕获所有异常
try:
    print(name)
except Exception as e:
    print(e)
"""

"""
异常else
else表示的是如果没有异常要执行的代码。
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，是没有异常的时候执行的代码')
"""

"""
异常的finally
finally表示的是无论是否异常都要执行的代码，例如关闭文件。
try:
    f = open('test.txt', 'r')
except Exception as e:
    f = open('test.txt', 'w')
else:
    print('没有异常，真开心')
finally:
    f.close()
"""