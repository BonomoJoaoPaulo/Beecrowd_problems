#include <iostream>

using namespace std;

int main() {

    int cp1, np1, cp2, np2;
    double vu1, vu2, value_to_pay;

    cin >> cp1 >> np1 >> vu1;
    cin >> cp2 >> np2 >> vu2;

    value_to_pay = (np1 * vu1 + np2 * vu2);

    cout << fixed;
    cout.precision(2);
    cout << "VALOR A PAGAR: R$ " << value_to_pay << endl;

    return 0;
}
