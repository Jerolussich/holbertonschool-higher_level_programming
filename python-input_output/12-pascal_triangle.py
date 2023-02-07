#!/usr/bin/python3
"""shebang"""


def pascal_triangle(n):
    """Create Pascal triangle."""

    triangle = [[0 for _ in range(-1, i)] for i in range(n)]
    new_triangle = triangle[:]

    for count in range(n):
        new_triangle[count][0] += 1

        for index, item in enumerate(triangle[count]):
            if (count == 2 and 1 <= index < len(new_triangle[count]) - 1):
                new_triangle[count][index] += (
                    new_triangle[count - 1][index - 1] +
                    new_triangle[count - 1][index - 1]
                )
            elif count >= 2 and index == len(new_triangle[count]) - 1:
                new_triangle[count][index] += 1
            elif count > 2 and 1 <= index < len(new_triangle[count]) - 1:
                new_triangle[count][index] += (
                    new_triangle[count - 1][index] +
                    new_triangle[count - 1][index - 1]
                )

        if count == 1:
            new_triangle[count][1] += 1

        triangle = new_triangle[:]

    return new_triangle
