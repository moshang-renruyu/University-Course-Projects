f=open("D:/bill.txt","r",encoding="UTF-8")
fw=open("D:/bill.txt.bak","w",encoding="UTF-8")
for line in f:
    line=line.strip()
    if line.split(",")[4]=="测试":
        continue

    fw.write(line)
    fw.write("\n")
f.close()
fw.close()




