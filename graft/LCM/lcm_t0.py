l1 = [2,2,2,3,3,5,7]
l2 = [2,3,3,3,5,5,11]
l3 = [3,3,7,13]


l4 = l1 + l2 + l3  #把每个数的因数列表组合成一个列表
l4 = list(set(l4))  #把组合后的列表元素去重

t = 1  #t1用于存储最终计算的那个因数

for i in range(len(l4)):  #用列表4中的所有元素逐个去l1,l2,l3中找相同元素的个数。
    s1 = l1.count(l4[i])
    s2 = l2.count(l4[i])
    s3 = l3.count(l4[i])
    s = [s1,s2,s3]  #把每个列表中找到的元素个数组合为一个新列表
    x = s.index(max(s))  #找到列表中最大的元素，最小公倍数是找因数在多个中共同出现次数最多的那个，然后相乘
    if s[x] != 0:  #如果出现次数不为0，那么就计算这个元素出现次数最多的那个次方。排除为0的情况下的计算
        t1 = l4[i] ** s[x]
        t = t * t1

print(t)

#判断有几个列表，因为列表数量是未知的。应该可以用列表嵌套来实现。