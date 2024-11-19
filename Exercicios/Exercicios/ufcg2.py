ten1 = int(input())
res1 = int(input())
ten2 = int(input())
res2 = int(input())
ten3 = int(input())
res3 = int(input())

cor1 = ten1 / res1
cor2 = ten2 / res2
cor3 = ten3 / res3

if cor1 > cor2 and cor1 > cor3:
    print('condutor com maior corrente: 1')
    if cor1 >= 1:
        print(f'maior corrente: {cor1:.2f} A')
    if cor1 >= 0.001 and cor1 < 1:
        cor11 = cor1 * 1000
        print(f'maior corrente: {cor11:.2f} mA')
    if cor1 >= 0.000001 and cor1 < 0.001:
        cor11 = cor1 * 1000000
        print(f'maior corrente: {cor11:.2} µA')
elif cor2 > cor1 and cor2 > cor3:
    print('condutor com maior corrente: 2')
    if cor2 >= 1:
        print(f'maior corrente: {cor2:.2f} A')
    if cor2 >= 0.001 and cor2 < 1:
        cor22 = cor2 * 1000
        print(f'maior corrente: {cor22:.2f} mA')
    if cor2 >= 0.000001 and cor2 < 0.001:
        cor22 = cor2 * 1000000
        print(f'maior corrente: {cor22:.2f} µA')
elif cor3 > cor1 and cor3 > cor2:
    print('condutor com maior corrente: 3')
    if cor3 >= 1:
        print(f'maior corrente: {cor3:.2f} A')
    if cor3 >= 0.001 and cor3 < 1:
        cor33 = cor3 * 1000
        print(f'maior corrente: {cor33:.2f} mA')
    if cor3 >= 0.000001 and cor3 < 0.001:
        cor33 = cor3 * 1000000
        print(f'maior corrente: {cor33:.2f} µA')