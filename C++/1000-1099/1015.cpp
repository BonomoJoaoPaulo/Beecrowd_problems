#include <iostream>
#include <math.h>

using namespace std;

int main(){
    double x1, y1, x2, y2, distance;

    cin >> x1 >> y1;
    cin >> x2 >> y2;
    
    distance = sqrt(pow(x2 - x1, 2.0) + pow(y2 - y1, 2.0));

    cout << fixed;
    cout.precision(4);
    cout << distance << endl;

    return 0;
}
