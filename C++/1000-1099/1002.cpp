#include <iostream>
#include <math.h>

using namespace std;

int main(){
    double r, n, area;
    n = 3.14159;
    cin >> r;
    
    area = pow(r, 2.00) * n;

    cout << fixed;
    cout.precision(4);
    cout << "A=" << area << endl;

    return 0;
}
