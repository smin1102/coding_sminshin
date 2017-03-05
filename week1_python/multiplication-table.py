# name = input("몇 단을 출력하시겠습니까?")
# print(int(name))
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in num_list:
#     print(str(name) + "*" + str(num) + "=" +int(name)**num)

dan=int(input("몇 단을 출력??"))
for num in range(1, 10):
    print("{} * {} = {}".format(dan, num, dan * num))
