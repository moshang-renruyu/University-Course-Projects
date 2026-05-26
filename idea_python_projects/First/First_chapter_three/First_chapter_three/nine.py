#1.构建一个随机的数字变量
import random
num=random.randint(1,10)
guess=int(input("请输入你猜测的数字："))
if guess==num:
    print("恭喜一次猜中")
else:
    if(guess>num):
        print("big")
    else:
        print("small")
    guess=int(input("请再次输入你猜测的数字："))
    if guess ==num:
        print("恭喜第二次即中")
    else:
        if guess >num:
            print("big")
        else:
            print("small")
    guess = int(input("请第三次次输入你猜测的数字："))
    if guess == num:
        print("恭喜第三次猜中")
    else:
        if guess > num:
            print("big")
        else:
            print("small")
