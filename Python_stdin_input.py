# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:55:44 2020

@author: Administrator
"""
'''
        多行连续读入问题，sys.stdin,input,sys.stdin.readline().strip()
'''
import sys
try:
    while True:
        line1 = sys.stdin.readline().strip()
        if line1 == '':
            break
        line2 = sys.stdin.readline().strip()
        a = int(line1)
        l = list(map(int, line2.split()))
        b = [int(n) for n in line2.split()]
        print(a)
        print(l)
        print(b)
except:
    pass

# ==========================================

# end = ''
# for line in iter(input,end):
# #    line1 = line.split()
# #    print(int(line1[1]) + int(line1[0]))
# # ---------------------------------------
#      lines = list(map(int,line.split()))
#      print(lines[0]+lines[1])
# ---------------------------------------
# import sys
# # 1.method1
# # for line in sys.stdin:
# #      a = line.strip().split()  #注意使用strip去掉空格和换行符，尤其是换行符。
# #      print(int(a[0]) + int(a[1]))
# # ---------------------------------------
# # 2. method2
# while True:
#      a = sys.stdin.readline().strip()
#      if a=='':  #注意判断位置，否则这里结束有问题。
#           break
#      else:
#           lines = list(map(int,a.split()))
#           print(lines[0]+lines[1])

# =========================================
#
# import sys
# if __name__ == "__main__":
#    # 读取第一行的n
#    n = int(sys.stdin.readline().strip())
#    ans = 0
#    for i in range(n):
#        # 读取每一行
#        line = sys.stdin.readline().strip()
#        # 把每一行的数字分隔后转化成int列表
#        values = list(map(int, line.split()))
#        print(values)
#        for v in values:
#            ans += v
#    print(ans)
#