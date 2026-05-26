"""
元组同列表一样,都是可以封装多个、不同类型的元素在内。
但最大的不同点在于：
元组一旦定义完成,就不可修改
所以,当我们需要在程序内封装数据,又不希望封装的数据被篡改,那么元组就非常合适了
元组定义：定义元组使用小括号,且使用逗号隔开各个数据,数据可以是不同的数据类型。
#定义元组字面量
（元素,元素,元素)
#定义元组变量
变量名称=（元素,元素,...元素)
#定义空元组
变量名称=（) #方式1
变量名称=tuple() #方式2
"""
t1=(1,'Hello',True)
t2=()
t3=tuple()
print(type(t1),t1)
print(type(t2),t2)
print(type(t3),t3)

t4=("Hello",)
print(type(t4),t4)
# 注意：元组只有一个数据,这个数据后面要添加逗号

#元组也支持嵌套：
t5=((1,2,3),(4,5,6))
print(type(t5),t5)
num=t5[1][2]
print(num)
"""
index()	查找某个数据,如果数据存在返回对应的下标,否则报错
count()	统计某个数据在当前元组出现的次数
len(元组)	统计元组内的元素个数
元组由于不可修改的特性,所以其操作方法非常少。
"""
#根据下标（索引)取出数据
t1 = (1, 2, "hello")
print(t1[2])#结果："hello’
#根据index（),查找特定元素的第一个匹配项
t1 = (1, 2,"hello", 3,4,"hel1o")
#结果：2
print(t1.index("hello"))
#统计某个数据在元组内出现的次数
t1 = (1, 2,'hello', 3,4,"hello")
print(t1.count('hello'))#结果：2
#统计元组内的元素个数
t1 = (1, 2, 3)
print(len(t1))# 结果3

"""
同列表一样，元组也可以被遍历。
可以使用while循环和for循环遍历它
"""
t8=("xue","jing","xuan")
index=0
while index <len(t8):
    print(t8[index]," ",end="")
    index+=1
print()
for element in t8:
    print(element)
"""
不可以修改元组的内容，否则会直接报错
可以修改元组内的list的内容（修改元素、增加、删除、反转等）
不可以替换list为其它list或其它类型
"""

"""
元组的特点
经过上述对元组的学习，可以总结出列表有如下特点：
可以容纳多个数据
可以容纳不同类型的数据（混装）
数据是有序存储的（下标索引）
允许重复数据存在
不可以修改（增加或删除元素等）
支持for循环
多数特性和list一致，不同点在于不可修改的特性。
"""

#作业
student=('薛婧萱',19,['football','music'])
print(student.index(19))
print(student[0])
del student[2][0]
print(student)
student[2].append("coding")
print(student)