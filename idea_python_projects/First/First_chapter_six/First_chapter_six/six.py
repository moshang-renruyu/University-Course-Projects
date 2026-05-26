"""
将容器内的元素依次取出进行处理的行为，称之为：遍历、迭代。
如何遍历列表的元素呢？
可以使用前面学过的while循环
如何在循环中取出列表的元素呢？
使用列表[下标]的方式取出
循环条件如何控制？
定义一个变量表示下标，从0开始
循环条件为 下标值 < 列表的元素数量
语法：
index = 0
while index < len（列表):
    元素=列表［index]
    对元素进行处理
    index += 1

除了while循环外，Python中还有另外一种循环形式：for循环。
对比while，for循环更加适合对列表等数据容器进行遍历。
语法：
for 临时变量 in 数据容器:
    对临时变量进行处理
表示，从容器内，依次取出元素并赋值到临时变量上。
在每一次的循环中，我们可以对临时变量（元素）进行处理。

while循环和for循环，都是循环语句，但细节不同：
在循环控制上：
while循环可以自定循环条件，并自行控制
for循环不可以自定循环条件，只可以一个个从容器内取出数据
在无限循环上：
while循环可以通过条件控制做到无限循环
for循环理论上不可以，因为被遍历的容器容量不是无限的
在使用场景上：
while循环适用于任何想要循环的场景
for循环适用于，遍历数据容器的场景或简单的固定次数循环场景

"""
def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    my_list=["xue","jing","xuan"]
    index=0
    while index<len(my_list):
        element=my_list[index]
        print(element)
        index+=1
list_while_func()
def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return: None
    """
    my_list = ["xue", "jing", "xuan"]
    for element in my_list:
        print(element)

list_for_func()

#作业
num=[1,2,3,4,5,6,7,8,9,10]
index=0

while index<len(num):
    if num[index]%2==0:
        print(num[index]," ",end="")
    index+=1
print()
for x in num:
    if x%2==0:
        print(x," ",end="")