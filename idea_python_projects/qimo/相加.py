"""
n=int(input())
s=0
s2=0
for i in range(2,n+1):
    s=1/i
    s2+=s
print("%.2f"%s2)
print(f'经计算，结果为{s2:.2f}')
print("经计算，结果为{:.2f}".format(s2))
"""

"""
n=int(input())
s=0
for i in range(2,n+1):
    s+=1.0/i
print(f'值为{s:.2f}')
print("值为{:.2f}".format(s))
print("值为%.2f"%s)
"""


