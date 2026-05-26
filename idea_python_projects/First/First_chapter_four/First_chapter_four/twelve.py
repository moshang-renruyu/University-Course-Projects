"""
continue关键字用于：中断本次循环，直接进入下一次循环
continue可以用于：    for循环和while循环，效果一致
break关键字用于：直接结束所在循环
break可以用于：    for循环和while循环，效果一致
注意事项：
continue和break，在for和while循环中作用一致
在嵌套循环中，只能作用在所在的循环上，无法对上层循环起作用
"""
# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")
    print("语句4")