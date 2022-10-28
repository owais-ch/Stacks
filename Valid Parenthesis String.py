'''Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true'''


class Solution:
    def checkValidString(self, s):
        num_left=0
        num_star=0

        stack1=[]
        stack2=[]
        length=len(s)
        num_right=0

        for i in range(length):
            if s[i]=='(':
                stack1.append([s[i],i])
                num_left+=1
            elif s[i]=='*':
                stack2.append([s[i],i])
                num_star+=1
            elif s[i]==')':
                if stack1!=[]:
                    stack1.pop()
                    num_left-=1
                elif stack2!=[]:
                    stack2.pop()
                    num_star-=1
                else:
                    return False
                
        #print(stack1,stack2)   
        
        while stack1!=[] and stack2!=[]:
            #print(stack1,stack2)  
            if stack1[0][1]<stack2[0][1]:
                stack1.pop(0)
                stack2.pop(0)
            else:
                
                stack2.pop(0)####return False
        if stack1!=[]:
            return False
        return True
