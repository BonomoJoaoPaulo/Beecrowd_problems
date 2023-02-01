#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int A, B, C, MAIOR;

    cin >> A >> B >> C;

    MAIOR = (A + B + abs(A-B))/2;
    MAIOR = (MAIOR + C + abs(MAIOR-C))/2;

    cout << MAIOR << " eh o maior" << endl;

    return 0;
}
