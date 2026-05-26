"""
1. 函数是：
组织好的、可重复使用的、用来实现特定功能的代码段
2. 使用函数的好处是：
将功能封装在函数内，可供随时随地重复利用
提高代码的复用性，减少重复代码，提高开发效率
"""
str1="xue"
str2="jing"
str3="xuan"
s=0
for i in str1:
    s+=1
print(s)
s=0
for i in str2:
    s+=1
print(s)
s=0
for i in str3:
    s+=1
print(s)

def mylen(data):
    s=0
    for i in data:
        s+=1
    print(s)
mylen(str1)
mylen(str2)
mylen(str3)