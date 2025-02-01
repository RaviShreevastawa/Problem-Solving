def main():
    n = int(input("Enter the value of n: "))
    fibonacci = 0
    for i in range (n+1):
        fibonacci = fibonacci+i
    print(fibonacci)
    
if __name__ == "__main__":
    main()