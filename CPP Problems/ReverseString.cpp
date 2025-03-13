using namespace std;
# include <iostream>
# include <string>
# include <algorithm>


int main(){
    // First Approach
    string str ;
    string rev ;

    cout<<"Enter a String : ";
    getline(cin, str);

    cout<<"The Entered String is :"<<str<<endl;

    for(int i = str.length()-1; i>=0; i--){
        rev += str[i];
    }
    cout<<"The Reversed String is : "<<rev<<endl;


    // the Second One using reverse function

    reverse(str.begin(), str.end());
    cout<<"The Reversed String is : "<<str<<endl;

    return 0;
}