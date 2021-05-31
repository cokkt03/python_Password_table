# !/usr/bin/python
# coding:utf-8
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
