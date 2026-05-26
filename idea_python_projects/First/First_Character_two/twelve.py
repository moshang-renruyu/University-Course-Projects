'''
字符串格式化 - 快速写法
通过语法：f"内容{变量}"的格式来快速格式化
这种写法不做精度控制
也不理会类型
适用于快速格式化字符串
'''
set_up_year=2006
stock_price=19.99
name2="哈理工"
print(f"我是{name2}，我成立于{set_up_year}今日股价为{stock_price}亿元")
