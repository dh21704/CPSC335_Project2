# Activity Selection

Algorithm 2

## Description
This project takes in a tuple of lists of acitivities with a start and finish time. It returns the maximum number of activities that do not ovberlap assuming a single person performs all activities. 


## Features

prints out the list of selected activities that maximize teh non overlapping participation

## Installation

1. need an online IDE
2. need the newest python installed

## Input

tup = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]

## Output

[(1, 3), (4, 6), (6, 7), (8, 9)]

## Algorithm Notes

Uses greedy algorithm and picks the next activity with teh earliest finishing time

Time: O(n log n)
Space O(n)
