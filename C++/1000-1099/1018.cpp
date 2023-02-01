#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int N, N_restante, n100, n50, n20, n10, n5, n2, n1;

    cin >> N;

    n100 = N/100;
    N_restante = N%100;

    n50 = N_restante/50;
    N_restante = N_restante%50;

    n20 = N_restante/20;
    N_restante = N_restante%20;

    n10 = N_restante/10;
    N_restante = N_restante%10;

    n5 = N_restante/5;
    N_restante = N_restante%5;

    n2 = N_restante/2;
    N_restante = N_restante%2;

    n1 = N_restante;

    cout << N << endl;
    cout << n100 << " nota(s) de R$ 100,00" << endl;
    cout << n50 << " nota(s) de R$ 50,00" << endl;
    cout << n20 << " nota(s) de R$ 20,00" << endl;
    cout << n10 << " nota(s) de R$ 10,00" << endl;
    cout << n5 << " nota(s) de R$ 5,00" << endl;
    cout << n2 << " nota(s) de R$ 2,00" << endl;
    cout << n1 << " nota(s) de R$ 1,00" << endl;

    return 0;
}
