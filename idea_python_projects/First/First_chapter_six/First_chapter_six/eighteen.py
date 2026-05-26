"""
数据容器的通用操作 - 遍历
数据容器尽管各自有各自的特点，但是它们也有通用的一些操作。

首先，在遍历上：
5类数据容器都支持for循环遍历
列表、元组、字符串支持while循环，集合、字典不支持（无法下标索引）
尽管遍历的形式各有不同，但是，它们都支持遍历操作。

除了遍历这个共性外，数据容器可以通用非常多的功能方法
len(容器)
统计容器的元素个数
max(容器)
统计容器的最大元素
min(容器)
统计容器的最小元素
通用排序功能
sorted(容器, [reverse=True]),reverse=True表示降序得到一个排好序的列表
注意，排序后都会得到列表（list）对象。
list()	转换为列表
tuple()	转换为元组
str()	转换为字符串
set()	转换为集合
注意：无法转为字典，因为字典是键值对
"""
mylist=[1,2,3,4,5,6]
mytuple=(1,2,3,4,5)
mystr="abcdefg"
myset={1,2,3,4,5,6}
mydict={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
#len()元素个数
print(f"列表元素个数有{len(mylist)}")
print(f"元组元素个数有{len(mytuple)}")
print(f"字符串元素个数有{len(mystr)}")
print(f"集合元素个数有{len(myset)}")
print(f"字典元素个数有{len(mydict)}")
#max()最大元素
print(f"列表最大元素有{max(mylist)}")
print(f"元组最大元素有{max(mytuple)}")
print(f"字符最大元素有{max(mystr)}")
print(f"集合最大元素有{max(myset)}")
print(f"字典最大元素有{max(mydict)}")
#min()最小元素
print(f"列表最小元素有{min(mylist)}")
print(f"元组最小元素有{min(mytuple)}")
print(f"字符最小元素有{min(mystr)}")
print(f"集合最小元素有{min(myset)}")
print(f"字典最小元素有{min(mydict)}")
#排序
print(f"列表对象的排序结果{sorted(mylist)}")
print(f"元组对象的排序结果{sorted(mytuple)}")
print(f"字符对象的排序结果{sorted(mystr)}")
print(f"集合对象的排序结果{sorted(myset)}")
print(f"字典对象的排序结果{sorted(mydict)}")
#反向排序
print(f"列表对象的反向排序结果{sorted(mylist,reverse=True)}")
print(f"元组对象的反向排序结果{sorted(mytuple,reverse=True)}")
print(f"字符对象的反向排序结果{sorted(mystr,reverse=True)}")
print(f"集合对象的反向排序结果{sorted(myset,reverse=True)}")
print(f"字典对象的反向排序结果{sorted(mydict,reverse=True)}")
