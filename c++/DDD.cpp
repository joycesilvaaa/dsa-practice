#include <stdio.h>
#include <iostream>
#include <map>

using namespace std;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    map<int, string> cidades = {{61, "Brasilia"}, {71, "Salvador"}, {11, "Sao Paulo"}, {21, "Rio de Janeiro"}, {32, "Juiz de Fora"}, {19, "Campinas"}, {27, "Vitoria"}, {31, "Belo Horizonte"}};

    int x;
    cin >> x;

    if (cidades.find(x) == cidades.end()) {
        cout << "DDD nao cadastrado" << endl;
    } else {
        cout << cidades[x] << endl;
    }
}