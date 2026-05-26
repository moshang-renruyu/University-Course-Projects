#1.构建一个随机的数字变量
import random
num=random.randint(1,100)
s=0
#通过一个布尔类型的变量，做循环是否继续的标志
flag=True
while flag:
     guess=int(input("请输入你猜测的数字："))
     s+=1
     if guess==num:
         print("恭喜猜中")
         #设置False就是循环终止条件
         flag=False
     else:
           if(guess>num):
               print("big")
           else:
               print("small")
print(f"你一共猜测{s}次")