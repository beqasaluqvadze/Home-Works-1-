###############################
#   სამწუხაროდ სამეცადინო დრო არმაქვს თითქმის საერთოდ მაქსიმალურად ვცდილობ შევისწავლო მაგრამ ხშირად მიწევს ხელოვნური
#   ინტელექტის დახმარება უშვალოდ როგორ უნდა დავწერო სწორად
# 1

def find_min_max(*args):
    return min(args), max(args)


minimum, maximum = find_min_max(1, 2, 3, 4, 5, 6)
print(minimum)
print(maximum)


#######################
# 2

def calculate(*args, operation):
    if operation == "sum":
        return sum(args)
    elif operation == "min":
        return min(args)
    elif operation == "max":
        return max(args)
    elif operation == "mult":
        multi_result = 1
        for i in args:
            multi_result *= i
        return multi_result
    else:
        print("Invalid operation")


##############################
# 3

print(calculate(1, 2, 3, 4, 5, operation="sum"))  # ხელოვნური ინტელექტი დავიხმარე
print(calculate(1, 2, 3, 4, 5, operation="max"))
print(calculate(1, 2, 3, 4, 5, operation="min"))
print(calculate(1, 2, 3, 4, 5, operation="mult"))


######################################
# 4


def format_user(first_name, last_name, **kwargs):
    full_name = f"{first_name} {last_name}"

    more_info = ""
    for key, value in kwargs.items():
        more_info += f"{key}: {value}"

    return f"{full_name} | {more_info}"


print(format_user(first_name="John", last_name="Smith", age=25, job="Developer"))


#########################
# 5
def safe_divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    else:
        return (a // b, a % b)


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, 1))
print(safe_divide(10, 3))
