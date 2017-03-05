
import random
menu_korean =("불고기", "김밥")
menu_chinese =("짜장면", "짬뽕")
menu_japanese =("스시", "돈부리")

# 한식, 중식, 일식 중 한 가지를 고르라는 내용
user_choice = input("Please choose from Korean, Chinese, and Japanese.")
print("I want " + user_choice)

# 그 중에서 한 가지를 고르면
if user_choice == "Korean":
    choice_result = random.choice(menu_korean)
    # choice_result = menu_korean(
    # random.randint(0, len(menu_korean))
    # )
elif user_choice == "Chinese":
    choice_result = random.choice(menu_chinese)
elif user_choice == "Japanese":
    choice_result = random.choice(menu_japanese)
else:
    print("Choose only from Korean, Chinese, and Japanese")

if choice_result:
    print("{} is chosen from {} food.".format(choice_result, user_choice))


# 식당 이름을 하나 임의로 추천
