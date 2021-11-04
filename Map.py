import numpy as np
from random import shuffle, randrange



#MOVEMENT_IN_MAP_DICTIONARY = {
#        "w": np.array([0, -2]),
#        "a": np.array([-2, 0]),
#        "s": np.array([0, 2]),
#        "d": np.array([2, 0]),
#        }


# class Tile:
#     def __init__(self, north):
#         self.north =
#         pass


class Map:
    def __init__(self):
        pass

#     def map_cords_to_normal_cords(self, map_cord):
#         return 

    ## FROM https://rosettacode.org/wiki/Maze_generation#Python
    def make_maze(self, w: int = 16, h: int = 8):
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
        hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

        ver2 = [[1] * w + ['1'] for _ in range(h)] + [[]]
        hor2 = [[1] * w + ['1'] for _ in range(h + 1)]

        # walls are 1 and corridors are 0
        maze = np.ones((h*2+1 , w*2+1))
        def to_my_ind(his_ind):
            return his_ind * 2 + 1

        def walk(x, y):
            vis[y][x] = 1

            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]: continue
                if xx == x:
                    hor[max(y, yy)][x] = "+  "
                    row = to_my_ind(max(y, yy))
                    col = to_my_ind(x)
                    ## GOD KNOWS WHY THIS WORKS
                    maze[row, col] = 0
                    maze[row-1, col] = 0
                    maze[row-2, col] = 0
                if yy == y:
                    ver[y][max(x, xx)] = "   "
                    row = to_my_ind(y)
                    col = to_my_ind(max(x, xx))
                    ## GOD KNOWS WHY THIS WORKS
                    maze[row, col] = 0
                    maze[row, col-1] = 0
                    maze[row, col-2] = 0
                walk(xx, yy)

        walk(randrange(w), randrange(h))

        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])

        return s, maze
