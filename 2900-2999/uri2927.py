A,C,X,Y = [int(x) for x in input().split()]

OFF = X+Y
ON = C - OFF

if A < ON:
    print('Igor feliz!')
else:
    if X > Y/2:
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')
    