#Sort an binary array in O(n) complexity (Linear search)
#Input - unsorted binary array
#Ouput - sorted binary array
#Ex - in - [1, 0, 1, 0, 0, 1, 1, 1, 0]  out - [0, 0, 0, 0, 1, 1, 1, 1, 1]

input = [1, 0, 1, 0, 0, 1, 1, 1, 0]
inp_len = len(input)
index = 0
for i in range(inp_len):
    if input[i] < 1:
        temp = input[index]
        input[index] = input[i]
        input[i] = temp
        index = index + 1
    i = 1 + 1

print(input)
