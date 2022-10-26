


def maxStackSum(stack1, stack2, stack3):
    sum1=sum(stack1)
    sum2=sum(stack2)
    sum3=sum(stack3)
    
    while stack1!=[] and stack2!=[] and stack3!=[]:
        if sum3==sum1 and sum1==sum2:
            return sum3
        elif sum3>=sum1 and sum3>=sum2:
            sum3=sum3-stack3.pop(0)
        elif sum2>=sum1 and sum2>=sum3:
            sum2=sum2-stack2.pop(0)
        elif sum1>=sum2 and sum1>=sum2:
            sum1=sum1-stack1.pop(0)
            
    return 0
