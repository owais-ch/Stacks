'''
Valid Expression
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', 
verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.

Example 1:

Input:
S = ()[]{}
Output: 1
Explanation: The arrangement is valid, as both the conditions are followed here.
'''

class Solution:
    def valid(self, s): 
        stack=[]
        length=len(s)
        
        for i in range(length):
            if s[i] in ["(","{","["]:
                stack.append(s[i])
            elif stack!=[]:
                if s[i]==")" and stack[-1]=="(":
                    stack.pop()
                elif s[i]=="}" and stack[-1]=="{":
                    stack.pop()
                elif s[i]=="]" and stack[-1]=="[":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
                    
        if stack==[]:
            return 1
            
        return 0
