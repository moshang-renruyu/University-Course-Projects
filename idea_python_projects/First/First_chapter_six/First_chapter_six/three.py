"""
1. 列表的下标索引是什么？
列表的每一个元素，都有编号称之为下标索引
从前向后的方向，编号从0开始递增
从后向前的方向，编号从-1开始递减
2. 如何通过下标索引取出对应位置的元素呢？
列表[下标]，即可取出
3. 下标索引的注意事项：
要注意下标索引的取值范围，超出范围无法取出元素，并且会报错
"""
#语法：列表[下标索引]
name_list = ['Tom', 'Lily', 'Rose']
#结果：Tom
print(name_list[0])
print(name_list[1])
#结果：Lily
print(name_list[2])# 结果：Rose

#语法：列表[标号]
name_list = ['Tom','Lily', 'Rose']
print(name_list[-1])
#结果：Rose
#结果：Lily
print(name_list[-2])
print(name_list[-3])# 结果：Tom

#2层嵌套list
my_list = [ [1, 2, 3], [4,5,6] ]
#获取内层第一个list
#结果：[1，2，3]
print(my_list[0])
#获取内层第一个list的第一个元素
#结果：1
print(my_list[0] [0])
