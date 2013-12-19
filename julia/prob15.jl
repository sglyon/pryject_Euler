"""
Project Euler Problem 15

Problem text:

    Starting in the top left corner of a 2 X 2 grid, there are 6 routes
    (without backtracking) to the bottom right corner.

    ![Alt text](../data/prob15_image.png)

    How many routes are there through a 20 X 20 grid?

Date: Wed Dec 18 14:38:25 MST 2013

"""
import Tools.pascal_row

euler15() = int(pascal_row(20 + 21)[21])
