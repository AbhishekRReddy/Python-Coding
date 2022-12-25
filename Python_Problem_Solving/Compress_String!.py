'''In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
string_input=input()
key=lambda x: x[0]
count=0
temp=string_input[0]
for i in range(len(string_input)):
    if(string_input[i]==temp):
        count+=1
        if(i==len(string_input)-1):
            print(f'({count}, {string_input[i]})')
        #prev_char=string_input[i]
    else:
        print(f'({count}, {temp})',end=' ')
        temp=string_input[i]
        count=1
        if(i==len(string_input)-1):
            print(f'(1, {string_input[i]})')
