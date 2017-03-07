# -*- coding: utf-8 -*-
# @Date    : 2017-03-05 20:30:49
# @Author  : Jeffei Cheung (jeffeicheung@gamil.com)
# @Link    : www.baidu.com

# A-Star algorithm

# grid format:
#   0 = navigable space
#   1 = occupied space
grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right
delta_name = ['^', '<', 'v', '>']
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1
# print(init,goal)

# h(x,y)<= dis([x,y],goal)
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
             # A-star al. heuristic function
# general search
heuristic1 = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]


def print_mat(A):
    for i in range(len(A)):
        print(A[i])


def a_star_search():
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    count = 0
    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h

    open = [[f, g, h, x, y]]  # h is not necessary

    found = False
    resign = False  # flag if we can or not expand

    # debug code
    print('initial open list')
    for i in range(len(open)):
        print(' ', open[i])
    print('------')
    while found is False and resign is False:
        # check open list
        if len(open) == 0:
            resign = True
            print('fail')
        else:
            open.sort(reverse=True)
            next = open.pop()
            x = next[3]
            y = next[4]
            g = next[1]

            expand[x][y] = count
            count += 1
            # check if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                # print(next)
                print('Successful')
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            # print([g2, x2, y2])
                            open.append([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2
    print_mat(expand)

if __name__ == '__main__':
    a_star_search()

# 有可能A*算法比一般search算法差。但当cell较多时，A*算法是首选。
