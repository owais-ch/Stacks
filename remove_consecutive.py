'''
Removing consecutive duplicates (GFG)

You are given string str. You need to remove the consecutive duplicates from the given string using a Stack.
 

Example 1:

Input: 
aaaaaabaabccccccc

Output: 
ababc

Explanation: 
The order is in the following way 6->a, 1->b, 2->a, 1->b, 7->c. 
So, only one element from each group will remain and rest all are removed.
Therefore, final string will be:- ababc.
'''

class Solution:
    
    #Function to remove consecutive duplicates from given string using Stack.
    def removeConsecutiveDuplicates(self,s):
        stack=[]
        length=len(s)
        
        for i in range(length):
            if stack==[]:
                stack.append(s[i])
            else:
                while stack!=[]:
                    if stack[-1]==s[i]:
                        stack.pop()
                    else:
                        break
                stack.append(s[i])
                
        return ''.join(stack)
