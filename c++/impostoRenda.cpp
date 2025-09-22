#include <stdio.h>
#include <iostream>
#include <iomanip>

using namespace std;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    double salario;
    float imposto = 0.0;
    cin >> salario;

    cout << fixed << setprecision(2);
    
    if (salario > 4500) {
        imposto = imposto + ((salario - 4500) * 0.28);
        salario = salario - (salario - 4500);
    }

    if (salario > 3000 && salario <= 4500) {
        imposto = imposto + ((salario - 3000) * 0.18);
        salario = salario - (salario - 3000);
    }

    if (salario > 2000 && salario <= 3000) {
        imposto = imposto + ((salario - 2000) * 0.08);
        salario = salario - (salario - 2000);
    }
    
    if (imposto == 0.0) {
        cout << "Isento" << endl;
    }
    else {
        cout << "R$ " << imposto << endl;
    }
}