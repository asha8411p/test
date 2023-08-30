def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number

def find_armstrong_numbers(limit):
    armstrong_numbers = []
    for num in range(1, limit + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

limit = 1000
armstrong_nums = find_armstrong_numbers(limit)
print("Armstrong numbers up to", limit, ":", armstrong_nums)
