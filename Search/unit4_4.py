# -*- coding: utf-8 -*-
# @Date    : 2017-03-05 22:56:12
# @Author  : Jeffei Cheung (jeffeicheung@gamil.com)
# @Link    : www.baidu.com


def print_mat(A):
    for i in range(len(A)):
        print(A[i])


def print_3Dmat(A):
    for i in range(len(A)):
        print_mat(A[i])
        print('-------------')

# grid format:
#   0 = navigable space
#   1 = occupied space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['^', '<', 'v', '>']
init = [4, 3, 0]  # [x,y,direction]
goal = [2, 0]

# the cost field has 3 vlaues: right turn, no turn, left turn
cost = [2, 1, 100]
action = [-1, 0, 1]
action_name = ['R', '#', 'L']
value = [[[999 for col in range(len(grid[0]))] for row in range(len(grid))],
         [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
         [[999 for col in range(len(grid[0]))] for row in range(len(grid))],
         [[999 for col in range(len(grid[0]))] for row in range(len(grid))]]
policy = [[[' ' for col in range(len(grid[0]))] for row in range(len(grid))],
          [[' ' for col in range(len(grid[0]))] for row in range(len(grid))],
          [[' ' for col in range(len(grid[0]))] for row in range(len(grid))],
          [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]]
policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

change = True
while change is True:
    change = False
    # go through all grid cell and cal. val.
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for orientation in range(4):
                if goal[0] == x and goal[1] == y:
                    if value[orientation][x][y] > 0:
                        change = True
                        value[orientation][x][y] = 0
                        policy[orientation][x][y] = '*'
                elif grid[x][y] == 0:
                    # cal the three ways to propagate val
                    for i in range(3):
                        o2 = (orientation + action[i]) % 4   # -1 % 4 == 3
                        x2 = x + forward[o2][0]
                        y2 = y + forward[o2][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) \
                                and grid[x2][y2] == 0:
                            v2 = value[o2][x2][y2] + cost[i]
                            if v2 < value[orientation][x][y]:
                                value[orientation][x][y] = v2
                                policy[orientation][x][y] = action_name[i]
                                change = True

x = init[0]
y = init[1]
orientation = init[2]
policy2D[x][y] = policy[orientation][x][y]
while policy[orientation][x][y] != '*':
    if policy[orientation][x][y] == '#':
        o2 = orientation
    elif policy[orientation][x][y] == 'R':
        o2 = (orientation - 1) % 4
    elif policy[orientation][x][y] == 'L':
        o2 = (orientation + 1) % 4
    x = x + forward[o2][0]
    y = y + forward[o2][1]
    orientation = o2
    policy2D[x][y] = policy[orientation][x][y]


print_mat(policy2D)
print('####################')
