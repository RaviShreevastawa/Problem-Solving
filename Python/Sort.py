def avarage(num):
    sum = 0
    total = len(num)
    print("Length of list is : ",total)
    for val in num:
        sum = sum + val
        print(f"Sum at index {val} is : ",sum)
    avg = sum/total
    
    print(avg)
if __name__ == '__main__':
    num = []
    n = int(input("Enter the Number : "))
    for i in range(n+1):
        element = int(input(f"enter the value of index {i} : "))
        num.append(element)
    print(num)
    avarage(num)
