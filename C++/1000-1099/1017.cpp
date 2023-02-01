#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int travel_time, average_speed, distance;
    double consume;

    cin >> travel_time;
    cin >> average_speed;

    distance = travel_time * average_speed;
    consume = distance/12.0;

    cout << fixed;
    cout.precision(3);
    cout << consume << endl;

    return 0;
}
