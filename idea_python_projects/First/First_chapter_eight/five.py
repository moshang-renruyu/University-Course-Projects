"""
1. 打开文件，通过a模式打开即可
f = open('python.txt', 'a')

# 2.文件写入
f.write('hello world')

# 3. 内容刷新
f.flush()

注意：
a模式，文件不存在会创建文件
a模式，文件存在会在最后，追加写入文件
可以使用”\n”来写出换行符

"""
f=open("D:/test1.txt","a",encoding="UTF-8")
f.write("\n高中")
f.flush()
f.close()