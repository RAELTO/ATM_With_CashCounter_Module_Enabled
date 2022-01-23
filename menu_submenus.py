def main_menu():
  elegir1 = int(input('''  DTM
  DINERO A TODO MOMENTO
  ------------------------------------------------
  [1] CUENTA DE AHORROS     [2] SERVICIOS DE GIROS
  [3] SALIR
  ------------------------------------------------
  Elija una opción válida: '''))
  return elegir1

def sub_menu1():
  elegir2 = int(input('''
  CUENTA DE AHORROS
  ------------------------------------------------
  [1] RETIRO           [2] CONSULTA DE SALDO
  [3] TRANSFERENCIA    [4] CANCELAR
  ------------------------------------------------
  Elija una opción válida: '''))
  return elegir2

def sub_menu2():
  elegir3 = int(input('''
  RETIRO
  ------------------------------------------------
  [1] 100           [2] 200
  [3] 300           [4] 400
  [5] 500           [6] 600
  [7] OTRO VALOR    [8] CANCELAR
  ------------------------------------------------
  Elija una opción válida: '''))
  return elegir3