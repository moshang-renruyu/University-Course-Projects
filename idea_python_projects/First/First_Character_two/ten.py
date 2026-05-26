#  字符串格式化的语法为
#  "%占位符"%变量
#  %s
#   %表示：我要占位
#   s表示：将变量变成字符串放入占位的地方
#所以，综合起来的意思就是：我先占个位置，等一会有个变量过来，我把它变成字符串放到占位的位置
name="黑马程序员"

average_salary=15000
print("学IT，来%s月薪为%s"%(name,average_salary))#注意%
#  %s为将内容转换为字符串，放入占位位置
#  %d为将内容换成整数，放入占位位置
#  %f为将内容换成浮点型，放入占位位置
set_up_year=2006
stock_price=19.99
name2="哈理工"
print("%s成立于%d年，今日股价为%d亿元"%(name2,set_up_year,stock_price))
