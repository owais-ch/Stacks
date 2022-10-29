'''Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"'''

from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s):
        length=len(s)

        stack1=[]
        num_left=0
        num_right=0
        for i in range(length):
            if s[i]!='(' and s[i]!=')':
                stack1.append(s[i])
            elif s[i]=='(':
                stack1.append(s[i])
                num_left+=1
            else:
                if num_left>num_right:
                    stack1.append(s[i])
                    num_right+=1
        stack3=[]
        deque1=deque()
        
        length2=len(stack1)
        num_left=0
        num_right=0
        for i in range(-1,-length2-1,-1):
            if deque1==deque() and stack1[i]=='(':
                pass
            elif deque1!=deque() and  stack1[i]=='(' and num_left<num_right:
                deque1.appendleft(stack1[i])
                stack3.append(stack1[i])
                num_left+=1
            elif stack1[i]==')':
                stack3.append(stack1[i])
                deque1.appendleft(stack1[i])
                num_right+=1
            elif stack1[i]!='(':
                stack3.append(stack1[i])
        return ''.join(stack3[::-1])
