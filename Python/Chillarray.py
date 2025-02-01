def main():
    rows = int(input("Enter the value of rows : "))
    cols = int(input("Enter the value of cols : "))

    arr = []

    for i in range (rows):
        row = []
        for j in range(cols):
            elements = int(input(f"Enter the number of rows {i+1}  and columns {j+1} "))
            row.append(elements)
        arr.append(rows)
    print("The 2D Array is this : ")
    for row in arr:
        print(row)

if __name__ == "__main__":
    main()