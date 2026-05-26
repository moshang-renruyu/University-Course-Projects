"""
在Python，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件，语法如下
open(name, mode, encoding)
name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。
mode：设置打开文件的模式(访问模式)：只读、写入、追加等。
encoding:编码格式（推荐使用UTF-8）
示例代码如下：
f = open('python.txt', 'r', encoding=”UTF-8)
# encoding的顺序不是第三位，所以不能用位置参数，用关键字参数直接指定
注意：此时的`f`是`open`函数的文件对象，对象是Python中一种特殊的数据类型，拥有属性和方法，可以使用对象.属性或对象.方法对其进行访问，后续面向对象课程会给大家进行详细的介绍。

模式	  描述
r	  以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w	  打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，
      原有内容会被删除。如果该文件不存在，创建新文件。
a	  打开一个文件用于追加。如果该文件已存在，新的内容将会被写入到已有内容之后。
      如果该文件不存在，创建新文件进行写入。
"""
a = open("D:/测试.txt", "r", encoding="UTF-8")
print(type(a))


"""
read()方法：
文件对象.read(num)
num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中
    所有的数据。

readlines()方法：
readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，
         其中每一行的数据为一个元素。
readline()方法：一次读取一行内容
for循环读取文件行
close() 关闭文件对象

"""
# print(f"读取内容:{a.read(10)}")
# print(f"读取内容:{a.read()}")
# print("-----------------------------")
# lines=a.readlines()
# print(type(lines))
# print(f"lines读取内容:{lines}")
# line1=a.readline()
# line2=a.readline()
# line3=a.readline()
# print(line1)
# print(line2)
# print(line3)
for i in a:
    print(i)

"""
with open 语法
with open("python.txt", "r") as f:
    f.readlines()

 通过在with open的语句块中对文件进行操作
可以在操作完成后自动关闭close文件，避免遗忘掉close方法
操作	                                    功能
文件对象 = open(file, mode, encoding)	打开文件获得文件对象
文件对象.read(num)	                    读取指定长度字节,不指定num读取文件全部
文件对象.readline()	                    读取一行
文件对象.readlines()	                    读取全部行，得到列表
for line in 文件对象	                    for循环文件行，一次循环得到一行数据
文件对象.close()	                        关闭文件对象
with open() as f	                    通过with open语法打开文件，可以自动关闭
"""


