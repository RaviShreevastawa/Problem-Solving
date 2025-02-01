def recursive(n):
    if n<0 :
        raise ValueError("The given number is invalid ")
    elif n==0 or n == 1:
        return 1
    return n*recursive(n-1)

n = int(input("enter the number that you want ot : "))
print("The factorial of given numbr is : ", recursive(n))