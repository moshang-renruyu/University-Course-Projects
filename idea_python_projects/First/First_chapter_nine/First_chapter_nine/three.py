"""
异常是具有传递性的
当所有函数都没有捕获异常的时候, 程序就会报错

"""
def func01():
   print("这是func01开始")
   num = 1/0
   print("这是func01结束")

def func02():
    print("这是func02开始")
    func01()
    print("这是func02结束")
def main():
    try:
        func02()
    except Exception as e:
        print(e)
main()
