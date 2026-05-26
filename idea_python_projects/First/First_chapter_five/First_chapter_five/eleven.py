money=5000000
name=None
name=input("请输入您的姓名：")
def query(show_header):
    if show_header:
         print("--------查询余额-------")
    print(f"{name},您好，您的余额剩余{money}元")

def saving(num):
    global money
    money+=num
    print("--------存款---------")
    print(f"{name},您好，您存款{num}元成功。")
    query(False)
def get_money(num):
    global money
    money -= num
    print("--------取款---------")
    print(f"{name},您好，您取款{num}元成功。")
    query(False)
def main():
    print("----------主菜单---------")
    print(name,"您好，欢迎来到薛婧萱银行ATM。请选择操作：")
    print("查询存款\t输入1")
    print("存款\t\t输入2")
    print("取款\t\t输入3")
    print("退出\t\t输入4")
    return input("请输入您的选择")
while True:
    keyboard_input =main()
    if keyboard_input=="1":
        query(True)
        continue
    elif keyboard_input == "2":
        num=int(input("请输入存款金额"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请输入取款金额"))
        get_money(num)
        continue
    elif keyboard_input == "4":
          print("欢迎下次光临")
          break