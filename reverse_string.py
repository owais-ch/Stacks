'''
Reverse a string using Stack (GFG)

You are given a string S, the task is to reverse the string using stack.

Example 1:

Input: S="GeeksforGeeks"
Output: skeeGrofskeeG
'''
def reverse(S):
  stack=[]
      
  S=list(S)
  
  length=len(S)
  
  i=0
  while i<length:
      stack.append(S[i])
      i+=1
  
  i=0
  
  while stack!=[]:
      S[i]=stack.pop()
      i+=1
  return ''.join(S)
