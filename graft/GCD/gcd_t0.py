""" x = 1541
#用于存储最终输出的因数列表
list1 = []
x1 = x
x2 = 0
print(x, "=", end=" ")

#for循环结束后，如果x1的值没有变化，也就是等于for循环前的x2，说明值已经没有可以整除的余地了，结束while循环。
while x2 != x1:
    x2 = x1

    for i in range(2,10):
        #找到最小能整除的数,且排除自身
        if x1 % i == 0 and x1 != i:
            #添加到最终的列表中
            list1[len(list1):] = [i]
            #找到可以整除的最小的数后，需要除以这个数后再开始找下一个能整除的数
            x1 = int(x1/i)
            break

list1[len(list1):] = [x1]
print(*list1, sep = " x ") """

import math

x = 453
#用于存储最终输出的因数列表
list1 = []
x1 = x
x2 = 0
print(x, "=", end=" ")

#for循环结束后，如果x1的值没有变化，也就是等于for循环前的x2，说明值已经没有可以整除的余地了，结束while循环。
while x2 != x1:
    x2 = x1
    for i in range(2,10):
        #找到最小能整除的数,且排除自身
        if x1 % i == 0 and x1 != i:
            #添加到最终的列表中
            list1[len(list1):] = [i]
            #找到可以整除的最小的数后，需要除以这个数后再开始找下一个能整除的数
            x1 = int(x1/i)
            break
if x1 != x:
    while x1 >= 121:
        for ii in range(11, int(math.sqrt(x1))+1):
            if x1%ii == 0:
                list1[len(list1):] = [ii]
                x1 = int(x1/ii)
                break


list1[len(list1):] = [x1]
print(*list1, sep = " x ")