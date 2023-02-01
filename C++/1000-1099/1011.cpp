#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int r;
    double volume, pi = 3.14159;
    cin >> r;
    
    volume = (4.0/3) * pi * pow(r, 3.00);

    cout << fixed;
    cout.precision(3);
    cout << "VOLUME = " << volume << endl;

    return 0;
}
