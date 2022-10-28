'''You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"'''

class Solution:
    def removeStars(self, s: str) -> str:
        stack1=[]

        length=len(s)

        for i in range(length):
            if s[i]!='*':
                stack1.append(s[i])
            else:
                if stack1!=[]:
                    stack1.pop()
        return ''.join(stack1)
