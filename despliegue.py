import menu_submenus as m_s #IMPORTA LOS SUBMENUS PARA ESTE MODULO
import retiro as re # importa el modulo retiro
import retiro_cajero as r_c
def despliegue(result1, clave, saldos, n_cuenta, code_giro, valor_giro, password, caja, valores):#USA LAS VARIABLES Y LISTAS DEL MAIN
    while True:
      # 'despliegue' ejecutará los cambios en las listas y sus respectivas operaciones segun lo que elija el usuario
      if result1 == 1:
        result2 = m_s.sub_menu1()#llama al submenu1 y guarda su valor en result2
        if result2 == 1:
          result3 = m_s.sub_menu2()# llama al submenu2
          r_retiro = re.retiro(result3)#llama el modulo de retiro y almacena su valor en r_retiro
          if r_retiro >= 10:
            print('  -----------------------------------------')
            if r_retiro % 10 == 0:
              p4ss = input('  Ingrese la clave de su cuenta: ')
              if p4ss in clave:
                if r_retiro <= saldos[clave.index(p4ss)] and r_retiro<=valores[0]*caja[0]+valores[1]*caja[1]+ valores[2]*caja[2]+valores[3]*caja[3]+valores[4]*caja[4]+valores[5]*caja[5]:
                  cantidad = r_retiro
                  rt = r_c.retirar_dinero(caja, valores, result3, cantidad)#Llama al modulo retiro_cajero 
                  saldos[clave.index(p4ss)]-= cantidad
                  print(f'  Saldo restante en la cuenta: {saldos[clave.index(p4ss)]:,} $')
                  print('  ------------------------------------------------')
                  if rt==[0, 0, 0, 0, 0, 0]:
                    print('\n  Favor ingresar una cantidad redondeada en billetes de 500, 200, 100, 50, 20, 10')
                    print('  -------------------------------------------------')
                  elif rt==[-1,-1,-1,-1,-1,-1]:
                    print ('  CAJERO SIN FONDOS PARA REALIZAR MAS TRANSACCIONES')
                    print('  -------------------------------------------------')
                  break
                else:
                  print('  SALDO INSUFICIENTE PARA RETIRAR')
                  break
              else:
                print('  ---------------------------------')
                print('  CLAVE INCORRECTA')
                print('  ////////////////////////////////')
                break
            else:
              print('  Ingrese valores multiplo de 10')
              print('  ///////////////////////////')
              break

          if result3 == 8:
            print('  REGRESANDO AL MENÚ PRINCIPAL...')
            print('  ///////////////////////////////')
            break
          else:
            print('  OPCION NO VALIDA')
            print('  ////////////////////////')
            break
        elif result2 == 2:
          print('  --------------------------------------')
          p4ss = input('  Ingrese su clave de cuenta: ')
          if p4ss in clave:
            print('  Clave correcta')
            print('  ------------------------------------')
            print(f'  Su saldo actual es: {saldos[clave.index(p4ss)]:,}$')
          else:
            print('  CLAVE INCORRECTA')
            print('  //////////////////////////')
            break
          break
        elif result2 == 3:
          p4ss = input('  Ingrese su clave de cuenta de origen: ')
          if p4ss in clave:
            print('  Clave válida')
            print(f'  Su saldo es: {saldos[clave.index(p4ss)]:,} $')
            dinero_t = int(input('  Ingrese la cantidad de dinero a transferir: '))
            if dinero_t <= saldos[clave.index(p4ss)]:
              destino = input('  Dígite el número de cuenta destino: ')
              if destino in n_cuenta:
                saldos[clave.index(p4ss)] -= dinero_t
                saldos[n_cuenta.index(destino)] += dinero_t
                print('  TRANSFERENCIA EXITOSA')
                break
              else:
                print('  ERROR - CUENTA DESTINO NO ENCONTRADA')
                print('  //////////////////////////////////')
                break
            else:
              print('  SALDO INSUFICIENTE')
              print('  /////////////////////////////')
              break
          else:
            print('  CLAVE INCORRECTA')
            break
        elif result2 == 4:
          print('  REGRESANDO AL MENÚ PRINCIPAL...')
          print('  ///////////////////////////////')
          break
      elif result1 == 2:
        print('  ---------------------------------------')
        code = input('  Ingrese el código de giro: ')
        if code in code_giro:
          print('  CODIGO VALIDO')
          print(f'  El valor del giro es: {valor_giro[code_giro.index(code)]:,}$')
          print('  -------------------------------------')
          account = input('''  Ingrese el número de cuenta  a donde desea enviar el giro: 
  ''')
          if account in n_cuenta:
            print('  Giro enviado correctamente')
            saldos[n_cuenta.index(account)] += valor_giro[code_giro.index(code)] 
            valor_giro[code_giro.index(code)] -= valor_giro[code_giro.index(code)]
            break
          else:
            print('  CUENTA NO ENCONTRADA')
            print('  /////////////////////////')
            break
        else:
          print('  CODIGO NO VALIDO')
          break
      elif result1 == 3:
        employee_pass = input('''  Ingrese la contraseña de personal autorizado
  : ''')
        if employee_pass in password:
          print('  VALID PASSWORD')
          print('  CUENTAS Y FONDOS:')
          print('  -------------------------------------')
          for item in n_cuenta:
            print(f'  Número de cuenta: {item}')
            print(f'  Saldo: {saldos[n_cuenta.index(item)]:,}$')
            print('  -------------------------------------')
          print('  GIROS ACTUALES CON FONDOS:')
          for item in valor_giro:
            if item > 0:
              value = item
              print(f'  Código de giro: {code_giro[valor_giro.index(value)]}')
              print(f'  Fondos: {valor_giro[valor_giro.index(value)]:,}$')
              print('  -------------------------------------')
          end = input('''Presione enter para apagar
          ''')
          end = 'off'
          result1 = end
          return result1
          break
        else:
          print('  CONTRASEÑA INCORRECTA')
          print('  //////////////////////////////////')
          break
      else:
        print('  OPCION NO VALIDA')
        print('  /////////////////////////////////')
        break