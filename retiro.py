def retiro(result3): # manipula los valores de retiro para ser llamados y usados en despliegue
  if result3 == 1:
    retiro = 100
  elif result3 == 2:
    retiro = 200
  elif result3 == 3:
    retiro = 300
  elif result3 == 4:
    retiro = 400
  elif result3 == 5:
    retiro = 500
  elif result3 == 6:
    retiro = 600
  elif result3 == 7:
    retiro = int(input('  Ingrese el valor a retirar: '))
  elif result3 == 8:
    retiro = 0
  else:
    retiro = 0
  return retiro
  