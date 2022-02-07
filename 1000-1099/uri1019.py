N = int(input())

n_hr = 0
n_min = 0

if N > 3600:
    n_hr = int(N / 3600)
    N = N % 3600

if N > 60:
    n_min = int(N / 60)
    N = N % 60

n_seg = N

print(f'{n_hr}:{n_min}:{n_seg}')
