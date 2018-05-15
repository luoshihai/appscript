class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("姓名: " + self.name + "年龄: " + str(self.age))


# 所有学生列表
students = []
for i in range(1, 4):
    name = input("请输入第%d个学生姓名:" % i)
    age = eval(input("请输入第%d个学生年龄:" % i))
    students.append(Student(name, age))

# 保存需要删除的学生列表
need_remove_students = []
for stu in students:
    if stu.age < 18:
        need_remove_students.append(stu)

# 遍历需要删除的学生列表   删除所有学生列表中的该学生
for stu in need_remove_students:
    if stu in students:
        students.remove(stu)

for stu in students:
    print(stu)


