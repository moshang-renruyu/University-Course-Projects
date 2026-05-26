"""
字符串是字符的容器，一个字符串可以存放任意数量的字符。
和其它容器如：列表、元组一样，字符串也可以通过下标进行访问
从前向后，下标从0开始
从后向前，下标从-1开始
同元组一样，字符串是一个：无法修改的数据容器。
所以：
修改指定下标的字符	（如：字符串[0] = “a”）
移除特定下标的字符	（如：del 字符串[0]、字符串.remove()、字符串.pop()等）
追加字符等		（如：字符串.append()）
均无法完成。如果必须要做，只能得到一个新的字符串，旧的字符串是无法修改

"""
str="itheima"
value=str[2]
print(value)
value=str[-5]
print(value)

"""
字符串的常用操作
查找特定字符串的下标索引值
语法：字符串.index(字符串)
"""
str2="xuejingxuan"
print(str2.index("e"))
"""
字符串的替换:
     语法：字符串.replace(字符串1，字符串2）
     功能：将字符串内的全部：字符串1，替换为字符串2
     注意：不是修改字符串本身，而是得到了一个新字符串哦
"""
str="xuejingxuan"
print(str.replace("x","j"))
"""
字符串的分割
     语法：字符串.split(分隔符字符串）
     功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
     注意：字符串本身不变，而是得到了一个列表对象
"""
str2="xue jing xuan"
print(str2.split(" "))
"""
字符串的规整操作（去前后空格）
     语法：字符串.strip()
字符串的规整操作（去前后指定字符串）
     语法：字符串.strip(字符串)
"""
str2=" xue jing xuan "
print(str2.strip())
str2="12xue jing xuan21"
print(str2.strip("12"))
"""
统计字符串中某字符串的出现次数
     语法：字符串.count(字符串)
"""
str2=" xue jing xuan "
print(str2.count("x"))
"""
统计字符串的长度
     语法：len(字符串)
数字（1、2、3...）
字母（abcd、ABCD等）
符号（空格、!、@、#、$等）
中文
均算作1个字符
"""
str2="xue jing xuan"
print(len(str2))
"""
同列表、元组一样，字符串也支持while循环和for循环进行遍历
"""
str2="xue jing xuan"
index =0
while index <len(str2):
    print(str2[index],end="")
    index+=1
print()
for i in str2:
    print(i,end="")

"""
作为数据容器，字符串有如下特点：
只可以存储字符串
长度任意（取决于内存大小）
支持下标索引
允许重复字符串存在
不可以修改（增加或删除元素等）
支持for循环

基本和列表、元组相同
不同与列表和元组的在于：字符串容器可以容纳的类型是单一的，只能是字符串类型。
不同于列表，相同于元组的在于：字符串不可修改
"""