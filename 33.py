count=0
s=input('请输入一行字符，以回车键结束\n')
for i in s:
    if i.isdecimal():
        count+=1
print(count)
