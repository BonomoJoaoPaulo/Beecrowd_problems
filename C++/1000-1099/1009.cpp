#include <iostream>

using namespace std;

int main(){
    string name;
    double salary, sales, total;

    cin >> name;
    cin >> salary;
    cin >> sales;

    total = salary + (sales * 0.15);

    cout << fixed;
    cout.precision(2);
    cout << "TOTAL = R$ " << total << endl;

    return 0;
}
