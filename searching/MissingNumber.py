# Find a missing number in a sorted array of positive numbers
# Input - list of sorted array
# Output - return Missing Number else return -1
# Ex-> in - [1, 2, 3, 4, 5, 7] out - 6

input = [1, 2, 3, 4, 5, 7]
inp_len = len(input)
inp_sum = sum(input)

# Method 1 - Calculate the sum of using length of array and substract with each element to get the remaining count
sum = round((inp_len + 2) * (inp_len + 1) / 2)
# print(inp_sum)
# print(sum)
print("missing number - " + str(sum - inp_sum))
