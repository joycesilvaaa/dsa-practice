#include <iostream>
#include <string>
using namespace std;

int main() {
	string a; 
    string b;
    cin >> a;
    cin >> b;
    
    int sizeOfa;
    int sizeOfb;
    sizeOfa = a.size();
    sizeOfb = b.size();
    cout << sizeOfa << " " << sizeOfb << endl;
    
    string aWithB;
    aWithB = a+b;
    
    cout << aWithB << endl;
    
    char c0 = a[0];
    char d0 = b[0];
    a[0] = d0;
    b[0] = c0;
    
    
    cout << a << " " << b << endl;

    return 0;
}