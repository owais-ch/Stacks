'''
Print Bracket Number (GFG POTD)

Given a string str, the task is to find the bracket numbers, i.e., for each bracket in str, return i if the bracket is the ith opening or closing bracket to appear in the string. 

 Examples:

Input:  str = "(aa(bdc))p(dee)"
Output: 1 2 2 1 3 3
Explanation: The highlighted brackets in
the given string (aa(bdc))p(dee) are
assigned the numbers as: 1 2 2 1 3 3.
Input:  str = "(((()("
Output: 1 2 3 4 4 5
Explanation: The highlighted brackets in
the given string (((()( are assigned
the numbers as: 1 2 3 4 4 5
'''

class Solution:
	def bracketNumbers(self, str):
        stack=[]
        
        length=len(str)
        
        i=0
        
        count_open=0
        list1=[]
        
        while i<length:
            if str[i]=='(':
                count_open+=1
                stack.append(count_open)
                list1.append(count_open)
            elif str[i]==')':
                value=stack.pop()
                list1.append(value)
            i+=1
            
        return list1
