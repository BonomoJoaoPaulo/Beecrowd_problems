#include <iostream>
#include <math.h>

using namespace std;

int main(){
    double A, B, C, TRIANGULO, CIRCULO, TRAPEZIO, QUADRADO, RETANGULO, pi = 3.14159;

    cin >> A >> B >> C;

    TRIANGULO = (A*C)/2;
    CIRCULO = pi * pow(C, 2.00);
    TRAPEZIO = (A+B)/2 * C; 
    QUADRADO = B*B;
    RETANGULO = A*B;

    cout << fixed;
    cout.precision(3);
    cout << "TRIANGULO: " << TRIANGULO << endl;
    cout << "CIRCULO: " << CIRCULO << endl;
    cout << "TRAPEZIO: " << TRAPEZIO << endl;
    cout << "QUADRADO: " << QUADRADO << endl;
    cout << "RETANGULO: " << RETANGULO << endl;
    return 0;
}
