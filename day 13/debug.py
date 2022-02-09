# # Reproduce the Bug
# from random import randint
# dice_imgs = {"1", "2", "3", "4", "5", "6"}
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# #Play Computer
# year = int(input("what's your year of birth?: "))
# if year > 1980 and year <= 1994:    # year <= 1994 because it is excluded
#     print("Your are a millenial")
# elif year > 1994:
#     print("You are a Gen Z.")

# #Fix the Errors
# age = input("How old are you?")   # type int error
# if age > 18:
# print("You can drive at age {age}.") # indent error

# # print is our friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))  # error
# total_words = pages * word_per_page
# print(total_words)

# # Use a debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)  # indent error
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])