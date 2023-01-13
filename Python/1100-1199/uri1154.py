soma = 0
count = 0

while True:
    x = input()
    x = int(x)
    if x >= 0:
        soma += x
        count += 1
    elif x < 0:
        break

media = soma/count

print("{:.2f}" .format(media))
