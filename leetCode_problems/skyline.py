"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

    lefti is the x coordinate of the left edge of the ith building.
    righti is the x coordinate of the right edge of the ith building.
    heighti is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Check for Skyline problem
"""

class Solution(object):

    #buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

    buildings = [[0, 2, 3] , [2, 5 ,3]]

    def getSkyline(self, buildings):
        building_list = list()
        height_list = [0]
        curr_height = 0
        answer_list = list()

        for (a, b, c) in buildings:
            building_list.append([a, -c])
            building_list.append([b, c])

        building_list.sort(key=lambda x: (x[0], x[1]))

        for (l, h) in building_list:

            if h < 0:
                height_list.append(abs(h))
                height_list.sort(reverse=True)
            else:
                height_list.remove(h)

            if curr_height != height_list[0]:
                ht = height_list[0]
                answer_list.append([l, ht])
                curr_height = ht

        print(answer_list)
        #return answer_list

    getSkyline(object, buildings)

#print("Hello")