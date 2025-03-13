using namespace std;
# include <iostream>
# include <string>

// Started Code 

int main () {
    string str;
    cout<<"Enter the String : ";
    getline(cin, str);
    cout<<"Entered String is : "<<str<<endl;

    // Operations of Strings Are Below 

    int size = str.size();
    cout<<"The Size of String is : "<<size<<endl;
    str.append("Good");
    cout<<"Updated Sring "<<str<<endl;

    str.insert(2,"A");
    cout<<"Updated String is : "<<str<<endl;

    if(str.empty()){
        cout<<"The string is Empty";
    }else{
        cout<<"The String is : "<<str<<endl;
    };

    str.erase(2,5);
    cout<<"The Updated String : "<<str<<endl;

    string str1 = str.substr(2,6);
    cout<<"The substring is : "<<str1<<endl;
}