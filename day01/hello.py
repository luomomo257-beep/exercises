print("hello 全栈AI")

print(str(123))

print(int("111"))

print(float("3.14"))

print(bool(1))

name = input("请输入你的名字：")
age = input("请输入你的年龄：")
address=input("请输入你的地址：")
aihao = input("请输入你的爱好：")

print(f"我是{name},今年{age}岁，来自{address},喜欢{aihao}")


temperature=input("请输入当前的温度:")

temperature = float(int(temperature)*1.9+32)
print(f"华氏温度{temperature:.1f}")

#"10" + 5 会报错还是输出 15？
# print("10"+5)
# 结果是报错，字符串不能跟数字相加

# bool(0) 和 bool("0") 分别是 True 还是 False？
#false true

#  变量 x = 5，if x = 5: 合法吗？
# 不合法，if x=5: 是给x赋值5，正确的是if x==5:



