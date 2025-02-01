def palindrome():
    n = int(input("Enter the number : "))

    original_number= str(n)

    reversed_number =  original_number[::-1]


    if original_number == reversed_number:
        print(f"{original_number} is a palindorme number 👍👍")
    else:
        print(f"{original_number} is not a palindrome number 😒😒😒")

palindrome()
