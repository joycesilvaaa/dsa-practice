#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;
 
int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    vector<string> meses = {
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    };

    int mes;
    string escolhido;

    cin >> mes;
    cout << meses[mes-1] << endl;
}