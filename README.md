Priya Khatri - 24056337 James Hu - 78869080

## Repository Structure
- src (source code directory)
  - hvlcs.py: Program with implementation of the Highest Value Longest Common Subsequence algorithm (uses recursion and memoization). Also contains the input parser and main functions.
  - 
- inputs (input directory)
  - contains all the input files (both user generated and included).
 
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
