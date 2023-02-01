#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int N, N_restante, horas, minutos, segundos;

    cin >> N;

    horas = N/3600;
    N_restante = N%3600;

    minutos = N_restante/60;
    N_restante = N_restante%60;

    segundos = N_restante;

    cout <<horas<<":"<< minutos<<":"<<segundos<< endl;

    return 0;
}
