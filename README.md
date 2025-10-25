# Activity Selection Algorithm 2

## Description
This project takes in a tuple of lists of acitivities with a start and finish time. It returns the maximum number of activities that do not ovberlap assuming a single person performs all activities. 


## Features

prints out the list of selected activities that maximize teh non overlapping participation

## Installation

1. need an online IDE
2. need the newest python installed

## Input

[(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]

## Output

[(1, 3), (4, 6), (6, 7), (8, 9)]

## Algorithm Notes

Uses greedy algorithm and picks the next activity with teh earliest finishing time

Time: O(n log n)
Space O(n)

# Skyline Algorithm 1

## Description
This project takes in an array of integers representing building heights and erturns two lists that includes indices of buildings visible from either the left or the right


## Features

returns two lists containing indices of buildings visible from the left or right

## Installation

1. need an online IDE
2. need the newest python installed

## Input

[3, 7, 8, 3, 6, 1]

## Output

[0, 1, 2]
[5, 4, 2]

## Algorithm Notes

Uses greedy algorithm and picks the next activity with teh earliest finishing time

Time: O(n log n)
Space O(log n)

## Author
Daniel Hernandez
