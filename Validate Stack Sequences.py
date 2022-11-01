'''Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations 
on an initially empty stack, or false otherwise.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.'''

class Solution:
    def validateStackSequences(self, pushed, popped):
        length=len(pushed)
        
        i=0
        j=0
        stack=[]
        
        while i<length:
            if pushed[i]==popped[j]:
                i+=1
                j+=1
            elif stack==[] and pushed[i]!=popped[j]:
                stack.append(pushed[i])
                i+=1
            elif stack!=[] and stack[-1]==popped[j]:
                stack.pop()
                #i+=1
                j+=1
            else:
                stack.append(pushed[i])
                i+=1
            
        if stack==[]:
            return True
        return stack==popped[j:][::-1]
