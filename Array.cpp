using namespace std;
# include <iostream>
# include <string>
#include <algorithm> 

int main (){
    string msg  = "Hello";

    cout<<"Before Reverse " <<msg<<endl;

    reverse(msg.begin(), msg.end());

    cout<<"After Reverse "<<msg<<endl;

    return 0;
}