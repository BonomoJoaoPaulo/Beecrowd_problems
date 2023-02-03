#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int n100, n50, n20, n10, n5, n2, m100, m50, m25, m10, m5, m1;
    double N;

    cin >> N;

    double N_integral;
    double N_fractional = modf(N, &N_integral);
    double N_integral_restante, N_fractional_restante;

    n100 = N_integral/100;
    N_integral_restante = N_integral - (n100*100);

    n50 = N_integral_restante/50;
    N_integral_restante = N_integral_restante - (n50*50);

    n20 = N_integral_restante/20;
    N_integral_restante = N_integral_restante - (n20*20);

    n10 = N_integral_restante/10;
    N_integral_restante = N_integral_restante - (n10*10);

    n5 = N_integral_restante/5;
    N_integral_restante = N_integral_restante - (n5*5);

    n2 = N_integral_restante/2;
    N_integral_restante = N_integral_restante - (n2*2);

    m100 = N_integral_restante;

    N_fractional = N_fractional * 100;

    m50 = N_fractional/50;
    N_fractional_restante = N_fractional - (m50*50);

    m25 = N_fractional_restante/25;
    N_fractional_restante = N_fractional_restante - (m25*25);

    m10 = N_fractional_restante/10;
    N_fractional_restante = N_fractional_restante - (m10*10);

    m5 = N_fractional_restante/5;
    N_fractional_restante = N_fractional_restante - (m5*5);

    m1 = N_fractional_restante;

    cout << "NOTAS:" << endl;
    cout << n100 << " nota(s) de R$ 100.00" << endl;
    cout << n50 << " nota(s) de R$ 50.00" << endl;
    cout << n20 << " nota(s) de R$ 20.00" << endl;
    cout << n10 << " nota(s) de R$ 10.00" << endl;
    cout << n5 << " nota(s) de R$ 5.00" << endl;
    cout << n2 << " nota(s) de R$ 2.00" << endl;
    cout << "MOEDAS:" << endl;
    cout << m100 << " moeda(s) de R$ 1.00" << endl;
    cout << m50 << " moeda(s) de R$ 0.50" << endl;
    cout << m25 << " moeda(s) de R$ 0.25" << endl;
    cout << m10 << " moeda(s) de R$ 0.10" << endl;
    cout << m5 << " moeda(s) de R$ 0.05" << endl;
    cout << m1 << " moeda(s) de R$ 0.01" << endl;

    return 0;
}
