money =10000
i=1
for i in range(1,21):
    import random
    score = random.randint(1,10)
    if score <5:
        print(f"员工{i}绩效分{score},不满足，不发工资，下一位")
        continue
    if money>=1000:
        money -= 1000
        print(f"员工{i}绩效分{score}，满足条件发工资,公司账户还剩{money}元")
    else:
        print(f"余额不足，当前余额：{money}元，不足以发工资，发不了，下个月再来")