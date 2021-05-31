""" import random
random.seed()  #设置随机种子数
    #设置种子选择空间
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
ls = [] #存取密码的列表
FirstPsw = "" #存取第一个密码的字符
 
while len(ls)<100:  #十个随机密码
    pwd = ""

    for i in range(8):
        pwd += s[random.randint(0,len(s)-1)]
    if pwd[0] in FirstPsw:
        continue
    else:
        ls.append(pwd)
        FirstPsw +=pwd[0]
    print(pwd)
fo = open("password.txt","w",encoding ="utf-8")
fo.write("\n".join(ls))
fo.close() """
import time
start = time.process_time()

for i in range(48,57):
    for j in range(48,57):
        for k in range(48,57):
            for l in range(48,57):
                for m in range(48,57):
                    for n in range(48,57):
                        for o in range(48,57):
                            for p in range(48,57):
                                        a=chr(i)+chr(j)+chr(k)+chr(l)+chr(m)+chr(n)+chr(o)+chr(p)
                                        print(a)
                                        fo = open("password.txt","w",encoding ="utf-8")
                                        fo.write("\n".join(a))
                                        fo.close()





end = time.process_time()

print("執行時間:%f 秒"%(end-start))
