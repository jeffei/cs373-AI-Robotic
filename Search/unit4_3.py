# -*- coding: utf-8 -*-
# @Date    : 2017-03-05 21:18:38
# @Author  : Jeffei Cheung (jeffeicheung@gamil.com)
# @Link    : www.baidu.com


# A-Star algorithm

# grid format:
#   0 = navigable space
#   1 = occupied space
grid = [[0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right
delta_name = ['^', '<', 'v', '>']
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost_step = 1
# print(init,goal)



def print_mat(A):
    for i in range(len(A)):
        print(A[i])



def dynamic_plan(grid):
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True
                elif grid[x][y] == 0: # is not obstacle
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) \
                                and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost_step
                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                policy[x][y] = delta_name[a]
    return value,policy


if __name__ == '__main__':
    value,policy = dynamic_plan(grid)
    print_mat(policy)
   # li = [2,3,1,5,4]
   # li.sort(reverse=True)
   # print(li.pop())

    a = (-1) % 4
    print(a)
# 有可能A*算法比一般search算法差。但当cell较多时，A*算法是首选。
