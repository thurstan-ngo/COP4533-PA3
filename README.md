# COP4533 Programming Assignment 3
Thurstan Ngo - 86963382  
Syed Rahman - 95234900

## Running the Program
Type `python3 main.py input_file.txt` into the terminal to run the program (python3 may not be the command setup on your machine in which case you need to use what your computer has it set to)

## Assumptions


## Question 1: Empirical Comparison


## Question 2: Recurrence Equation
Let OPT(i, j) = max value of the longest common subsequence  
Let val($x_i$) = value of character $x_i$
$$
OPT(i,j) = 
\begin{cases} 
0 & \text{if }i = 0 \text{ or } j = 0 \\
OPT(i-1, j-1) + val(x_i) & \text{if } x_i = y_j \\
\text{max} (OPT(i-1, j) \text{, } OPT(i, j-1)) & \text{otherwise} \\
\end{cases}
$$
The recurrence is correct. The base cases indicate that if either string has a length of 0, then the value of the HVLCS is 0. If the current characters $x_i$ and $y_j$ match, then take the max value of the longest common subsequence up to the previous indices and add the value of the current character. Otherwise, skip one character from either string and take the max value of the two subsequences.


## Question 3: Big-Oh

