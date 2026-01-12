# 作者: 王道 龙哥
# 2024年12月26日16时10分28秒
# xxx@qq.com

my_list = [x for x in range(10)]

print(my_list)
print('-'*50)
# 2个for循环
a = [j for i in range(10) for j in range(i)]
print(a)
print('-'*50)
# 二维列表
# 二维列表生成式，[[内层循环的列表] for row in range(5)]外面的【】代表外层循环
# 这里的col * row是每一个最里面元素的值，col * row for col in range(5)代表内层循环每次针对同一个row不同的col做col*row操作
# for row in range(5)代表外层循环每次变的值是row
a = [[col * row for col in range(5)] for row in range(5)]
print(a)
print('-'*50)
# print(a[1][2])
# 二维转一维
# 一维的生成式，j是最后生成的列表中的每一个元素，for x in a是外层循环，for j in x是内层循环，x代表a中的每一个元素（列表）
b = [j for x in a for j in x]
print(b)
print('-'*50)
# 使用if
c = [x for x in range(10) if x % 2 == 0]
print(c)
print('-'*50)
# 使用if else
d = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(d)
print('-'*50)