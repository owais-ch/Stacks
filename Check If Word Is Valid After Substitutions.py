'''Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

 

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.'''

class Solution:
    def isValid(self, s: str) -> bool:
        length=len(s)

        stack1=[]
        count=0

        for i in range(length):
            stack1.append(s[i])
            count+=1

            if count>=3:
                #print(stack1[-1:-4:-1][::-1])
                if stack1[-1:-4:-1][::-1]==['a','b','c']:
                    count1=0

                    while count1<3:
                        stack1.pop()
                        count-=1
                        count1+=1
                    
        if stack1==[]:
            return True
        return False
