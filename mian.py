##############
# 1
##############

random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in random_list:
    sum += i
    print(sum)


#############
# 2 აქაც დამჭირდა რომე ლექციისთვის მეყირებინა თავიდან და აი ისთვის მეკითხა მაგრამ ლოგიკა გავიგე   და გავაკეთე
#############


numbers = [5,20,45,67,85,12,30,100]

max_number = numbers[0]
min_number = numbers[0]

for i in numbers:
    if max_number < i:
        max_number = i
    if min_number > i:
        min_number = i

print(max_number)
print(min_number)
print(numbers)

#############
# 3
############# დამჭირდა ai გამოყენება ვერ გავიხსენე კოდი როდის იღებდა ლუწს და კენტს სორტირება გამახსენდა თქვენი ახნილიდან
#მეტი სილამაზისთვის


numbers = [1, 25, 34, 67, 23, 45, 66, 88, 92, 22, 12]
numbers.sort()
odd = []
even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    if i % 2 != 0:
        odd.append(i)

print(even)
print(odd)
print(numbers)

############
#4
############


number_lst = [1,2,3,4,5,6,7,8,]
tuple_number = tuple(number_lst)

print(tuple_number)
print(type(tuple_number))
print(number_lst)
print(type(number_lst))

###########
#5
###########

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
set = set(lst)

print(lst)
print(type(lst))
print(set)
print(type(set))




