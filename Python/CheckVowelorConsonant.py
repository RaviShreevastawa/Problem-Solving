def check(str):
    vowels = 'aeiouAEIOU'

    for ch in (str):
        if vowels.isalpha():
            if(ch in vowels):
                print(f"{ch} is a vowel ")

            else:
                print(f"{ch} is a consonant ")

def main():
    str = input("Enter the string which have the vowels and consonant : ")
    check(str)

if __name__ == "__main__":
    main()