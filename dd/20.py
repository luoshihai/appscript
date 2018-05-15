result = input("请输入一个数:")

temp_list = list(result)
temp_list.reverse()

new_result = "".join(temp_list)

if result == new_result:
    print("你输入的是回文数")
else:
    print("不是回文数")
