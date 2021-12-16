# CS570-final-project

The final project of CSCI 570 Analysis of Algorithms Fall 2021: Implement the sequence alignment algorithm with dynamic programming approach and memory efficient approach (dynamic programming + divide and conquer).

Problem statement: Give two string, A and B, find the minimum cost of sequence alignment. Valid operations include insertiong and modifidying a single charater. The cost of inserting any char is beta, the cost of modifidying char i to char j is alpha(i, j). What is the minimum cost of alignment these two string, i.e. using valid operations to make these two string identical? 

The basic dp version of sequence alignment algorithm (see my post [Dynamic Programming Revisit](https://kaiwang.co/2021/11/04/dynamic-programming-revisit/) is capable to find the numerical answer in O(m*n) time, but in order to find the actually assignment/alignment, it need O(m*n) space.

The memory efficient version of sequence alignment used a combination of divide and conquer and dp. Used O(m*n) time but only O(m + n) space.
