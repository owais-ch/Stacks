'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each 
asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
'''

class Solution:
    def asteroidCollision(self, s):
        length=len(s)

        stack=[]

        for i in range(length):
            if stack==[]:
                stack.append(s[i])
            else:
                count=0
                visited='no'
                while stack!=[]:
                    if (stack[-1]>0 and s[i]<0) :
                        if abs(stack[-1])<abs(s[i]):
                            stack.pop()
                            visited='yes'
                            #stack.append(s[i])
                            #break
                        elif abs(stack[-1])==abs(s[i]):
                            stack.pop()
                            visited='no'
                            break
                        else:
                            visited='no'
                            break
                    elif (stack[-1]>0 and s[i]>0) or (stack[-1]<0 and s[i]<0) \
                    or (stack[-1]<0 and s[i]>0):
                        stack.append(s[i])
                        break
                    else:
                        break
                    count+=1
                    
                if visited=='yes' and stack==[]:
                    stack.append(s[i])
                

        return stack
    
