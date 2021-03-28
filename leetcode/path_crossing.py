# https://leetcode.com/problems/path-crossing/
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east,
# or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return True if the path crosses itself at any point, that is, if at any time you are on a location
# you've previously visited. Return False otherwise.
#
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.

class Solution(object):
    def isPathCrossing(self, path):
        x = y = 0
        dots = [(x,y)]

        for i in path:
            print(i)
            if i == 'E':
                x += 1
            elif i == 'W':
                x -= 1
            elif i == 'S':
                y -= 1
            elif i == 'N':
                y += 1
            else:
                print('Error')
                break
            print((x, y))
            if (x,y) in dots:
                print(dots)
                return True
            dots.append((x,y))
        return False


    if __name__ == '__main__':
        path = "NESWW"
        f = isPathCrossing(0,path)
        print(f)
