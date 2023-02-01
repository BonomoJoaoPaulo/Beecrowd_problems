#include <iostream>

using namespace std;

int main(){
    int X;
    double Y, CONSUMO;

    cin >> X;
    cin >> Y;
    CONSUMO = X/Y;

    cout << fixed;
    cout.precision(3);
    cout << CONSUMO << " km/l" << endl;

    return 0;
}
