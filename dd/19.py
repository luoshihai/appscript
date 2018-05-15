sum_number = eval(input("请输入你要输入多少个数:"))
i = 0

num = []

while i < sum_number:
    num.append(eval(input("请输入第%d个数" % (i+1))))
    i += 1
num.sort()
print(num)