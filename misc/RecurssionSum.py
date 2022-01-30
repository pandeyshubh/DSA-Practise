# Recursion add numbers from 1 till the given input
# Ex-> in = 5 out = 15

input = 5
result = 0

def sum_number(num):
    if num <= 1:
        return num
    else:
    #result = result + num
        return num + sum_number(num - 1)

#result =

def sum_number_test(num, result):
    if num == 0:
        return result

    result = result + num
    return sum_number_test(num - 1, result)

print(sum_number(input))
#print(sum_number_test(input, result))