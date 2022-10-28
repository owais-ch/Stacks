'''Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the 
smallest in lexicographical order among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        length=len(s)

        stack1=[]
        num_left=0
        num_right=0
        list1=[]
        for i in range(length):
            if s[i]=='(':
                stack1.append(s[i])
                num_left+=1
            else:
                num_right+=1
                if num_left==num_right and stack1!=[]:
                    stack1.pop(0)
                    list1.append(stack1)
                    stack1=[]
                    num_left=0
                    num_right=0
                else:
                    stack1.append(s[i])
        return ''.join(list(map(lambda x:''.join(x),list1)))
