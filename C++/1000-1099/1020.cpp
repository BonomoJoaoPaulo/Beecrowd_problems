#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int N, N_restante, years, months, days;

    cin >> N;

    years = N/365;
    N_restante = N%365;

    months = N_restante/30;
    N_restante = N_restante%30;

    days = N_restante;

    cout << years << " ano(s)" << endl;
    cout << months << " mes(es)" << endl;
    cout << days << " dia(s)" << endl;

    return 0;
}
