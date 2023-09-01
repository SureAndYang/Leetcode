#!/usr/bin/python3

""" Easy, Big Countries.

MySQL problem.
"""

# Write your MySQL query statement below
select name, population, area from World where area >= 3000000 or population >= 25000000;

