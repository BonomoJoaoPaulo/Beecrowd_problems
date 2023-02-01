#include <iostream>

using namespace std;

int main(){
    int number, hours;
    float hour_value, salary;

    cin >> number;
    cin >> hours;
    cin >> hour_value;

    salary = hours * hour_value;

    cout << "NUMBER = " << number << endl;
    cout << fixed;
    cout.precision(2);
    cout << "SALARY = U$ " << salary << endl;

    return 0;
}
