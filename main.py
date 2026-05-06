# #################################
# # 1
n = int(input('write positive number'))

while n >= 0:
    print(n, end=' ')

    n -= 1
print()
print('complete')
#
# ###############
# # 2
# ###############
#
# #### დავიხმარე ხელოვნური ინტელექტი გამახსენდა რომ True უსასრულო ციკლის დორს გამოიყენება
#
#
total = 0

while True:
    number = int(input('write positive number'))
    if number == 0:
        break
    if number != 0:
        print('try again')
    total += number

print(total)

####################
# 3
####################

secret_number = 7
while secret_number == 7:
    user_number = (input('write a number'))
    if user_number == 7:
        break
    if int(user_number) < 7:
        print('to low')
    elif int(user_number) > 7:
        print('to high')
    else:
        secret_number = user_number
        print('correct')

#########
# 4
#########
user_word = input("Enter a word: ").strip().lower()
vowels = ["a", "e", "i", "o", "u"]

for word in user_word:
    if word in vowels:
        continue
    print(word, end='')

print()

##########
# 5
##########

for a in range(0, 10):
    print(a, end=' ')
print()
for b in range(5, 16):
    print(b, end=' ')
print()
for c in range(0, 20, 2):
    print(c, end=' ')
print()
for d in range(10, 0, -1):
    print(d, end=' ')
print()
