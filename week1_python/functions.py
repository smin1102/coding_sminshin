# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print("hello, {}".format(name))

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"
name5 = "marco"
name6 = "jane"
name7 = "john"
name8 = "tom"

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)


# 1) parameters O return O
def sum(a, b):
    return a + b

# 2) parameters O return X
def hello_friends(name):
    print("hello, {}".format(name))

# 3) parameters X return O
def return_1():
    return 1

# 4) parameters X return X
def hello_world():
    print("hello world")

# num_1 = return_1()
# print(num_1)
