num = int(input())

if num > 0:
    for div in range(1, num):
        if num % div == 0:
            print(div)