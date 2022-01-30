#Partial working code - SkyLine Code
class Solution(object):

    #buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

    buildings = [[0, 2, 3] , [2, 5 ,3]]


    def isValid(current_ht, ans_list):

        ans_list[len(ans_list)] == current_ht

    def getSkyline(self, buildings):
        building_list = list()
        height_list = [0]
        curr_height = 0
        answer_list = list()

        for (a, b, c) in buildings:
            #if not building_list.__contains__([a, c]):
            building_list.append([a, -c])
            #if not building_list.__contains__([b, c]):
            building_list.append([b, c])

        building_list = sorted(building_list, key=lambda x: x[0])
        print(building_list)

        for (l, h) in building_list:

            if h < 0:
                height_list.append(abs(h))
                height_list.sort(reverse=True)
            else:
                height_list.remove(h)
                #print("heelo")

            if curr_height != height_list[0]:
                ht = height_list[0]
                answer_list.append([l, ht])
                curr_height = ht

           # if b < 0:
            #    b = abs(b)
             #   if b not in height_list:
              #      height_list.append(b)
               #     height_list.sort(reverse=True)

                #if b == height_list[0] and curr_height != b:
                 #   answer_list.append([a, b])
                  #  curr_height = b
                #b = -b
            #if b > 0:
             #   if b in height_list:
              #      if b == height_list[0] and curr_height != b:
               #         answer_list.append([a, height_list[0]])
                #        curr_height = b
                 #   height_list.remove(b)


        print(answer_list)

    getSkyline(object, buildings)

#print("Hello")