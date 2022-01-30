# FreeCodeCamp.org Algorithmic questions
# Symmetric Difference - From the given input set, create an output set with unique numbers
# Ex-> in [1, 2, 3] , [3, 4] out - [1, 2, 4]

inp_1 = [1, 4, 8] # input list 1
inp_2 = [1, 3, 2] # input list 2
map = {} # dictionary to load list data and check if item is repeated.

#without any inbuild functions
def insert_in_dict(inp):
    for i in range(len(inp)):
        if (map.__contains__(inp[i])):
            map.pop(inp[i])
        else:
            map.__setitem__(inp[i], 0)

insert_in_dict(inp_1)
insert_in_dict(inp_2)

#Inbuild set functionality
mySet = set(inp_1)
print(mySet.symmetric_difference(inp_2))
print(list(map.keys()))
