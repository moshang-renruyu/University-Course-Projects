'''
字符串格式化 - 表达式的格式化
刚刚的演示，都是基于变量的。
可是，我想更加优雅些，少写点代码，直接对“表达式”进行格式化是否可行呢？
那么，我们先了解一下什么是表达式。

表达式：一条具有明确执行结果的代码语句
如：
1 + 1、5 * 2，就是表达式，因为有具体的结果，结果是一个数字
又或者，常见的变量定义：
name = “张三”     age = 11 + 11
等号右侧的都是表达式呢，因为它们有具体的结果，结果赋值给了等号左侧的变量。
在无需使用变量进行数据存储的时候，可以直接格式化表达式，简化代码哦
'''
print("1*1的结果是：%d"%(1*1))
print(f"1*1的结果是：{1*1}")
print("字符串在Python中的类型是：%s"%type("字符串"))

'''
练习：股价计算
定义如下变量：
name，公司名
stock_price，当前股价
stock_code，股票代码
stock_price_daily_growth_factor，股票每日增长系数，浮点数类型，比如1.2
growth_days，增长天数
计算，经过growth_days天的增长后，股价达到了多少钱
使用字符串格式化进行输出，如果是浮点数，要求小数点精度2位数。
'''
name="哈理工"
stock_price=19.99
stock_code="00001"
stock_price_daily_growth_factor=1.2
growth_days=7
final_stock_price=stock_price * stock_price_daily_growth_factor ** growth_days
#**代表乘方
print("%.2f"%final_stock_price)
