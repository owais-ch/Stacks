'''
Removing consecutive duplicates - 2

You are given string str. You need to remove the pair of duplicates.
Note: The pair should be of adjacent elements and after removing a pair the remaining string is joined together. 

Example 1:

Input:
aaabbaaccd

Output: 
ad

Explanation: 
Remove (aa)abbaaccd =>abbaaccd
Remove a(bb)aaccd => aaaccd
Remove (aa)accd => accd
Remove a(cc)d => ad
'''

class Solution:
    
    #Function to remove pair of duplicates from given string using Stack.
    def removePair(self,s):
        length=len(s)
        stack=[]
        
        for i in range(length):
            if stack==[]:
                stack.append(s[i])
            else:
                while stack!=[]:
                    if stack[-1]==s[i]:
                        stack.pop()
                        break
                    else:
                        stack.append(s[i])
                        break
                    
        if stack==[]:
            return 'Empty String'
        return ''.join(stack)
