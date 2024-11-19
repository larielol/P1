start = 8.8
stop = 100.0
step = 0.2
sequencia = int((stop - start) / step)
for i in range(sequencia + 1):
    resultado = start + (i * step)
    print(f'{resultado:.1f}')