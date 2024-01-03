def add(*numbers):
    # result = 0
    # for num in numbers:
    #     result += num
    # return result
    return sum(numbers)


def subtraction(*other_num, first_num):
    for num in other_num:
        first_num -= num
    return first_num


def division(num, divider):
    return num/divider


def multiplication(num, multiplier):
    return num*multiplier
