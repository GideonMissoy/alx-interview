#!/usr/bin/python3
"""
Function returns a list of lists of integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    '''Fxn creats a list of lists on integers representing the pascal triangle
    '''
    p_triangle = []
    if type(n) is not int or n <= 0:
        return p_triangle
    for x in range(n):
        ln_lst = []
        for y in range(x + 1):
            if y == 0 or y == x:
                ln_lst.append(1)
            elif x > 0 and y > 0:
                ln_lst.append(p_triangle[x - 1][y - 1] + p_triangle[x - 1][y])
        p_triangle.append(ln_lst)
    return p_triangle
