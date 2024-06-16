'''
Get Min Pop (GFG)
Now, we'll try to solve a famous stack problem.
You are given an array A of size N. You need to first push the elements of the array into a stack and then print minimum in the stack at each pop until stack becomes empty.

Example 1:

Input:
N = 5
A = {1 2 3 4 5}
Output: 
1 1 1 1 1
Explanation: 
After pushing elements to the stack, 
the stack will be "top -> 5, 4, 3, 2, 1". 
Now, start popping elements from the stack
popping 5: min in the stack is 1.popped 5
popping 4: min in the stack is 1. popped 4
popping 3: min in the stack is 1. popped 3
popping 2: min in the stack is 1. popped 2
popping 1: min in the stack is 1. popped 1
'''

def _push(a,n):
    min_arr=[]
    
    for i in range(n):
        if i==0:
            min_arr=[a[i]]
            minimum=a[i]
        else:
            if a[i]<minimum:
                minimum=a[i]
                min_arr.append(minimum)
            else:
                min_arr.append(minimum)
    return min_arr


#Function to print minimum value in stack each time while popping.    
def _getMinAtPop(stack):
    while stack!=[]:
        value=stack.pop()
        print(value,end=' ')
        
