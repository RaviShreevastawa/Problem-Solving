#include <iostream>
#include <string>

using namespace std;

void checkPalindrome(string str);

int main() {
    string input;
    cout << "Enter a String: ";
    getline(cin, input);
    
    checkPalindrome(input); 
    return 0;
}

void checkPalindrome(string str) {
    string rev = "";

    for (int i = str.length() - 1; i >= 0; i--) {
        rev += str[i];
    }
    
    cout << "The Reversed String is: " << rev << endl;

    if (str == rev) {
        cout << "The Given String is a Palindrome." << endl;
    } else {
        cout << "The Given string is not a palindrome." << endl;
    }
}
