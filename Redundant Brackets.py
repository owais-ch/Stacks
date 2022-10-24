'''Given a valid mathematical expression in the form of a string, You are supposed to return true if the given expression contains redundant brackets else return False.
The given string only contains ')','(','+','-','*','/' and lower case english letters. 

def findRedundantBrackets(s:str):
    length=len(s)
    
    stack=[]
    
    for i in range(length):
        if s[i]!=')':
            stack.append(s[i])
        else:
            visited='no'
            while stack!=[] and s[i]==')' and stack[-1]!='(':
                if stack[-1] in ['+','-','*','/']:
                    visited='yes'
                stack.pop()
            if stack!=[] and stack[-1]=='(':
                stack.pop()
            if visited=='no':
                return True
    return False
