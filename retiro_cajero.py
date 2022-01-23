def retirar_dinero(caja, valores, result3, cantidad):
    dinero_caja = valores[0]*caja[0]+valores[1]*caja[1]+ valores[2]*caja[2]+valores[3]*caja[3]+valores[4]*caja[4]+valores[5]*caja[5]
    print(f'  DINERO EN CAJERO: {(dinero_caja-cantidad):,} $')
    if dinero_caja-cantidad<=0:
      dinero_caja = 0
    print('  --------------------------------------')
    print('  --------------------------------------')
    if cantidad <= dinero_caja:
      b500 = cantidad//500
      cantidad = cantidad % 500
      if b500 >= caja[0]:
        cantidad +=(b500-caja[0])*500
        b500 = caja[0]
 
      b200 = cantidad//200
      cantidad = cantidad % 200
      if b200 >= caja[1]:
        cantidad+=(b200-caja[1])*200
        b200 = caja[1]
 
      b100 = cantidad//100
      cantidad = cantidad % 100
      if b100 >= caja[2]:
        cantidad+=(b100-caja[2])*100
        b100 = caja[2]
 
      b50 = cantidad//50
      cantidad = cantidad % 50
      if b50 >= caja[3]:
        cantidad+=(b50-caja[3])*50
        b50 = caja[3]
 
      b20 = cantidad//20
      cantidad = cantidad % 20
      if b20 >= caja[4]:
        cantidad+=(b20-caja[4])*20
        b20 = caja[4]

      b10 = cantidad//10
      cantidad = cantidad % 10
      if b10 >= caja[5]:
        cantidad+=(b10-caja[5])*10
        b10 = caja[5]
 
      if cantidad == 0:
        caja[0]-=b500
        caja[1]-=b200
        caja[2]-=b100
        caja[3]-=b50
        caja[4]-=b20
        caja[5]-=b10
        print('  Retiro exitoso')
        print(f'\n\n  Billetes en cajero: \n  500: {caja[0]} \n  200: {caja[1]} \n  100: {caja[2]} \n  50: {caja[3]} \n  20: {caja[4]} \n  10: {caja[5]}')
        return [b500, b200, b100, b50, b20, b10]
      else:
        return [0, 0, 0, 0, 0, 0]
    else:
      return [-1, -1, -1, -1, -1, -1]