my_cat_name = 'miu'
my_cat_is_girl = True
my_cat_age = 2
my_cat_leght = 15.5

print(type(my_cat_name))
print(type(my_cat_is_girl))
print(type(my_cat_age))
print(type(my_cat_leght))

#2

year = input('enter birth year: ')
year = int(year)
year = 2026 - year
print('your age is', year)

#3
number = input('enter number: ')
number = int(number)
negative = number < 0
positive = number > 0
zero = number == 0
even = number % 2 == 0
odd = number % 2 != 0

print('negative:', negative)
print('positive:', positive)
print('zero:', zero)
print('even:', even)
print('odd:', odd)

