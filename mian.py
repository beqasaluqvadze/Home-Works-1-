###################
1

user_age = input("Enter your age: ")
user_age = int(user_age)

if user_age <= 12:
    print('kid')
elif user_age <= 18:
    print('teenager')
elif user_age <= 50:
    print('adult')
else:
    print('elder')

###2

student_score = input("Enter your score 0-100: ")
student_attendance = input("Enter your attendance 0-100%: ")

student_score = int(student_score)
student_attendance = int(student_attendance)

if student_score >= 60 and student_attendance >= 75:
    print(f"your score are {student_score} ,{student_attendance},you pass")
else:
    print(f"your score are {student_score} ,{student_attendance},you fail")

#########
# 3
student = input('are you student? yes/no')
member = input('are you member? yes/no')

if student == 'yes' and member == 'yes':
    print('you have aditional discount')
elif student == 'yes' or member == 'yes':
    print('you have discount')
else:
    print('you have not discount')


# 4

username = input("Enter your username: ")
username1 = (len(username))

if 3 <= username1 <= 20:
    username = username.isalnum()
    if username:
        print('username is valid')
    else:
        print('username is invalid')
else:
    print('username is invalid')
