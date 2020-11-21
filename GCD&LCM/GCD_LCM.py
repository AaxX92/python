# 注释规范相关：注释尽量使用行注释，即在函数/变量上一行，而不是紧跟其后。
def my_prime_factorization(x):
    # 用于存储最终输出的因数列表
    list1 = [] 
    x1 = x
    x2 = 0

    # TODO: 修改该算法，比如169的素因子是13，该算法显然得到错误结果。思考：range的范围？能不能加入list1前就去重？
    # NOTE: 改动了这个算法后，下面两个函数也记得做相应修改
    # for循环结束后，如果x1的值没有变化，也就是等于for循环前的x2，说明值已经没有可以整除的余地了，结束while循环。
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
    return list1



def gcd_count(num1,num2,num3):
    l1 = num1 + num2 + num3
    l1 = list(set(l1))  #把组合后的列表元素去重
    t = 1  #t用于存储最终计算的那个因数

    for i in range(len(l1)):  #用列表4中的所有元素逐个去l1,l2,l3中找相同元素的个数。
        s1 = num1.count(l1[i])
        s2 = num2.count(l1[i])
        s3 = num3.count(l1[i])
        s = [s1,s2,s3]  #把每个列表中找到的元素个数组合为一个新列表
        x = s.index(min(s))  #找到列表中最小的元素，最小公约数是找因数在多个中共同出现次数最少的那个，然后相乘，包括出现次数0次的。
        if s[x] != 0:  #如果出现次数不为0，那么就计算这个元素出现次数最少的那个次方。排除为0的情况下的计算
            t1 = l1[i] ** s[x]
            t = t * t1
    return t


def lcm_count(num1,num2,num3):
    l1 = num1 + num2 + num3
    l1 = list(set(l1))  #把组合后的列表元素去重
    t = 1  #t用于存储最终计算的那个因数

    for i in range(len(l1)):  #用列表4中的所有元素逐个去l1,l2,l3中找相同元素的个数。
        s1 = num1.count(l1[i])
        s2 = num2.count(l1[i])
        s3 = num3.count(l1[i])
        s = [s1,s2,s3]  #把每个列表中找到的元素个数组合为一个新列表
        x = s.index(max(s))  #找到列表中最大的元素，最小公倍数是找因数在多个中共同出现次数最多的那个，然后相乘
        if s[x] != 0:
            t1 = l1[i] ** s[x]
            t = t * t1
    return t