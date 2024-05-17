'''
Easy String (GFG)

You are given the string S . Compress the string when lower and upper cases are the same. In compressed string characters should be in lowercase.

Example 1:

Input: S = "aaABBb"
Output: "3a3b"
Explanation: As 'a' appears 3 times
consecutively and 'b' also 3 times,
and 'b' and 'B' considered as same. 
â€‹Example 2:

Input: S = "aaacca"
Output: "3a2c1a"
Explanation: As 'a' appears 3 times
consecutively and 'c' also 2 times,
and then 'a' 1 time.
'''

class Solution:
    def transform(self, S):
        n=len(S)
        count=0
        string=''
        
        count=1
        
        for i in range(1,n):
            if S[i].lower()==S[i-1].lower():
                count+=1
            else:
                string=string+str(count)+S[i-1].lower()
                count=1
        if count>0:
            string=string+str(count)+S[n-1].lower()
            
        return string
