"""
列表除了可以：
定义
使用下标索引获取值
以外,列表也提供了一系列功能：
插入元素
删除元素
清空列表
修改元素
统计元素个数
等等功能,这些功能我们都称之为：列表的方法
如果将函数定义为class（类）的成员,那么函数会称之为：方法

"""
# 列表的查询功能（方法）
# 查找某元素的下标
#      功能：查找指定元素在列表的下标,如果找不到,报错ValueError
#      语法：列表.index(元素)
#        index就是列表对象（变量）内置的方法（函数）
mylist=["itcast","itheima","python"]
print(mylist.index("itcast"))
# 列表的修改功能（方法）
# 修改特定位置（索引）的元素值：
#      语法：列表[下标] = 值
#      可以使用如上语法,直接对指定下标（正向、反向下标均可）的值进行：重新赋值（修改）
#正向下标
my_list = [1,2,3]
my_list[0] = 5
#结果：[5,2,3]
print(my_list)
#反向下标
my_list = [1,2,3]
my_list[-3] = 5
print(my_list)
#结果：[5,2,3]


# 插入元素：
#      语法：列表.insert(下标, 元素),在指定的下标位置,插入指定的元素
my_list = [1,2,3]
my_list.insert(1,5)
print(my_list)

# 追加元素：
#      语法：列表.append(元素),将指定元素,追加到列表的尾部
my_list = [1, 2,3]
my_list.append(4)
print(my_list)
#结果：[1,2,3,4]
my_list = [1,2,3]
my_list.append([4,5,6])
# 结果：［1,2,3,[4,5,6]]
print(my_list)

# 追加元素方式2：
#      语法：列表.extend(其它数据容器),将其它数据容器的内容取出,依次追加到列表尾部
my_list = [1,2,3]
my_list.extend([4, 5, 6])
print(my_list)
#结果：[1, 2,3,4, 5, 6]

# 删除元素：
#      语法1： del 列表[下标]
#      语法2：列表.pop(下标)
my_list = [1,2,3]
#方式1
del my_list[0]
print(my_list)
#结果：[2,3]
#方式2
my_list = [1,2,3]
my_list.pop(0)
#结果：[2,3]
print(my_list)

# 删除某元素在列表中的第一个匹配项
#      语法：列表.remove(元素)
my_1ist = [1,2,3,2,3]
my_1ist.remove(2)
#结果：[1,3,2,3]
print(my_1ist)

# 清空列表内容,语法：列表.clear()
my_list = [1,2,3]
my_list.clear()
#结果：[]
print(my_list)

# 统计某元素在列表内的数量
#      语法：列表.count(元素)
my_list = [1, 1, 1, 2, 3]
#结果：3
print(my_list.count(1))

# 统计列表内,有多少元素
#      语法：len(列表)
#      可以得到一个int数字,表示列表内的元素数量
my_1ist = [1, 2,3,4, 5]
#结果5　
print(len(my_list))
