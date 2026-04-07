Priya Khatri - 24056337 James Hu - 78869080

## Repository Structure
- src (source code directory)
  - hvlcs.py: Program with implementation of the Highest Value Longest Common Subsequence algorithm (uses recursion and memoization). Also contains the input parser and main functions.
  - 
- tests (test directory)
  - contains all the input files (both user generated and included).
  - Also contains the corresponding output files for each input file. 
 
## Getting Started
Make sure you can run Python code in your environment.
Clone the repository: `git clone https://github.com/priya2004k/Highest-Value-Longest-Common-Sequence.git`

## Input Specifications
The input file format is as follows:

K  
x1 v1  
x2 v2  
...  
xK vK  
A  
B  
K: number of distinct characters with assigned values
Each of the next K lines contains:
a character xi
its corresponding integer value vi
A: first string
B: second string

## Output Specifications
The program outputs:

`<maximum value>`  
`<optimal subsequence>`

First line: maximum total value of a common subsequence
Second line: one optimal subsequence achieving that value

## Running the Code
To Run HVLCS on an input file
Move your input file into the input/ directory, then run:

`python src/runner.py inputs/YOUR_INPUT_FILE.in`

If no input file is provided, the function will run on the default `test1.in` file. 


## Question 2: Recurrence Equation

We define our recurrence in a recursive function called dp which takes in parameters i and j. Our dp function aims to find out the highest value of a common subsequence between A[0, i-1] and B[0, j-1]. 

Our base case is when either i == 0 or j == 0 which represents an empty string. In this case, we return 0 since there can not be a common subsequence with an empty string.

Our recursive case has 2 possible scenarios: 
1. If A[i-1] == B[j-1] we can include this character in our longest subsequence since it matches for both strings. In this case, we add the characters value to our value counter and then call the dp function recursively and decrease both i and j by 1. 
2. We skip the current character from both strings by calling the dp function dp(i-1, j) and dp(i, j-1) and take the maximum value of those. 

We use a memoization dictionary to store results of each (i, j) indexes in order to avoid repeat work and lower the time complexity. 

We can prove that this algorithm is optimal using proof by exchange. Assime that there is some optimal solution called OPT and our solution will be called DP. 
At any index i, j, if A[i-1] != B[j-1], OPT will make the choice to exclude one of the last characters from either A or B since both can't be used in the highest value common subsequence. Therefore our algorithm DP will come up with a solution that is equally good, if not better to OPT because it checks both subproblems (i-1, j) and (i, j-1) and takes the max of both. 
Additionally at any index i, j, if A[i-1] == B[j-1] then the OPT algorithm can either choose to include the character at those indexes into the LCS or not. In this scenario DP will perform the same or better than OPT because DP explores both choices where it adds the character to the value count for LCS and also skips the character, and DP will take the max of those two choices. 
So, we can replace OPT(i, j) with DP(i, j) and not decrease the perfomrance of the optimal algorithm. This means that our DP algorithm is optimal. 
