
#!/usr/bin/python


n = int(raw_input('Intruduzca el numero de intervalos (n > 0): '))
PI = 3.1415926535897931159979634685441852

suma = 0
i0 = 0
while n <= 0:
  print 'El numero de intervalos debe ser mayor que 0'
  n = int(raw_input('Intruduzca otro numero de intervalos (n > 0): '))
  
for i1 in range(1, n+1):
  x_i = (i1 - 0.5) / float(n)
  fx_i = 4 / (1 + x_i * x_i)
  suma = suma + fx_i
  print 'Subintervalo: [%3.2f,%3.2f]    x_i: %4.3f    fx_i: %7.6f' % (i0/float(n), i1/float(n), x_i, fx_i)
  i0 = i1
print 'El valor aproximado de PI es:    %15.14f' % (1/float(n)*suma)
print 'El valor de PI con 35 decimales: %36.35f'% PI
    