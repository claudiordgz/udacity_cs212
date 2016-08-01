"""
Save Beta Rabbit
================

Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of rooms. In the center of each room (except for
the top left room) is a hungry zombie. In order to be freed, and to avoid being eaten, Beta Rabbit must move through
this grid and feed the zombies.

Beta Rabbit starts at the top left room of the grid. For each room in the grid, there is a door to the room above,
below, left, and right. There is no door in cases where there is no room in that direction. However, the doors are
locked in such a way that Beta Rabbit can only ever move to the room below or to the right. Once Beta Rabbit enters a
room, the zombie immediately starts crawling towards him, and he must feed the zombie until it is full to ward it off.
Thankfully, Beta Rabbit took a class about zombies and knows how many units of food each zombie needs be full.

To be freed, Beta Rabbit needs to make his way to the bottom right room (which also has a hungry zombie) and have used
most of the limited food he has. He decides to take the path through the grid such that he ends up with as little food
as possible at the end.

Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at the end, given
that he takes a route using up as much food as possible without him being eaten, and ends at the bottom right room. If
there does not exist a route in which Beta Rabbit will not be eaten, then return -1.

food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 200.

grid will be a list of N elements. Each element of grid will itself be a list of N integers each, denoting a single row
of N rooms. The first element of grid will be the list denoting the top row, the second element will be the list
denoting second row from the top, and so on until the last element, which is the list denoting the bottom row. In the
list denoting a single row, the first element will be the amount of food the zombie in the left-most room in that row
needs, the second element will be the amount the zombie in the room to its immediate right needs and so on. The top left
room will always contain the integer 0, to indicate that there is no zombie there.

The number of rows N will not exceed 20, and the amount of food each zombie requires will be a positive integer not
exceeding 10.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) food = 7
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 0

Inputs:
    (int) food = 12
    (int) grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
Output:
    (int) 1
"""

import math
from random import randrange
import functools


def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer

get_node = lambda x, ROWS, COLS: (int(math.floor(x/ROWS)), x % ROWS) if x != 0 else (0,0)


def build_adjacency_list(ROWS, COLS):
    adj_l, count = [], 0
    for i, _ in enumerate(range(ROWS*COLS)):
        node, el = set(), get_node(i, ROWS, COLS)
        r, c = el[0], el[1]
        last_column, last_row = c == COLS - 1, r == ROWS - 1
        last_column_and_row = last_column and last_row
        if last_column_and_row:
            pass
        elif last_column:
            node.add(i+COLS)
        elif last_row:
            node.add(i+1)
        else:
            node.update([i+COLS, i+1])
        adj_l.append(node)
    return adj_l


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for node in graph[vertex] - set(path):
            if node == goal:
                yield path + [node]
            else:
                stack.append((node, path + [node]))


def inefficient_dfs_answer(food, grid):
    """ Uses DFS to retrieve all the paths from the top left
        cell to the bottom right cell, then calculates the cost of
        each path and substracts the available coins. Stops if a
        path costs 0
    :param food: Available food (up to 200)
    :param grid: N x N grid up to 20 x 20
    :return: The minimal amount of food available or -1
    """
    ROWS, COLS = len(grid), len(grid[0])
    adj_list = build_adjacency_list(ROWS, COLS)
    final_cost = 999
    for path in dfs_paths(adj_list, 0, len(adj_list)-1):
        matrix_path = map(lambda x: get_node(x, ROWS, COLS), path)
        path_cost = sum(map(lambda (x,y): grid[x][y], matrix_path))
        cost = food - path_cost
        if -1 < cost < final_cost:
            final_cost = cost
            if cost == 0:
                return final_cost
    return final_cost if final_cost != 999 else -1


def answer(food, grid):
    @memoize
    def search(f, row, column):
        f -= grid[row][column]
        if row < 0 or column < 0 or f < 0:
            return food + 1
        elif row == column == 0:
            return f
        else:
            return min(search(f, row - 1, column), search(f, row, column - 1))
    remainder = search(food, len(grid) - 1, len(grid) - 1)
    return remainder if remainder <= food else -1


def test():
    N = 20
    data = [(
        7,
        [[0, 2, 5], [1, 1, 3], [2, 1, 1]],
        0
    ),(
        12,
        [[0, 2, 5], [1, 1, 3], [2, 1, 1]],
        1
    ),(
        200,
        [[randrange(1, 6) for _ in range(N)] for _ in range(N)],
        None
    )]
    for food, grid, r in data:
        result = answer(food, grid)
        print(result == r if r else result)


test()

