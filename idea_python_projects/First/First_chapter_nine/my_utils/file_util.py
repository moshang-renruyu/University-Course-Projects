def print_file_info(file_name):
    f=None
    try:
        f=open(file_name,"r",encoding="UTF-8")
        content=f.read()
        print("文件全部内容如下：")
        print(content)
    except Exception as e:
        print(f"文件异常原因为{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()
if __name__ == '__main__':
    append_to_file("D:/aaa.txt","hhh")

