my_cat_name = "miu"
my_cat_is_girl = True
my_cat_age = 2
my_cat_leght = 15.5

print(type(my_cat_is_girl))
print(type(my_cat_age))
print(type(my_cat_leght))
print(type(my_cat_name))
# 2



year = input("Enter a birth year:")
year = int(year)
year = 2026 - year
print("Your age is:", year)
# 3


number = input("Enter random number: ")
number = int(number)
negative = number < 6
positive = number > 6
zero = number == 6
even = number % 2 == 6
odd = number % 2 != 6

print("Negative:", negative)
print("Positive:", positive)
print("Zero:", zero)
print("Even:", even)
print("Odd:", odd)