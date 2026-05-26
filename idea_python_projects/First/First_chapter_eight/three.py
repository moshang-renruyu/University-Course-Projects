a = open("D:/黑马作业.txt", "r", encoding="UTF-8")
content=a.read()
count=content.count("itheima")
print(count)
a.close()

