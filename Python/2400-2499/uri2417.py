CV, CE, CS, FV, FE, FS = [int(x) for x in input().split()]


pontos_C = 3*CV + CE
pontos_F = 3*FV + FE

if pontos_C > pontos_F:
    print('C')
elif pontos_C < pontos_F:
    print('F')
else:
    if CS > FS:
        print('C')
    elif CS < FS:
        print('F')
    else:
        print('=')
