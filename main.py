import menu_submenus as m_s # Importa el menú principal
import despliegue as desp # importa la función despliegue
print('''
  _____   _______    ___   _   _  _ _  __
 | _ \ \ / /_   _|__| _ ) /_\ | \| | |/ /
 |  _/\ V /  | ||___| _ \/ _ \| .` | ' < 
 |_|   |_|   |_|    |___/_/ \_\_|\_|_|\_\
                                         
''')# esto es de adorno :v jaja
n_cuenta = [
  '0021052539', '9083050198', '0173960710', 
  '7900419721', '0099105407', '5000871539'
] 
clave = ['1234', '9978', '6158', '0552', '1120', '0191']
saldos = [10000, 800, 25000, 1900, 30000, 100]

code_giro = ['6798', '0715', '7803', '1105']
valor_giro = [150, 8400, 70, 900]

password = ['MANY21M05', 'BANGR21Y07M'] #CLAVES DEL PERSONAL AUTORIZADO

caja = [10, 10, 10, 10, 10, 10]
valores = [500, 200, 100, 50, 20, 10]

while True:
  result1 = m_s.main_menu()
  ejecutar = desp.despliegue(result1, clave, saldos, n_cuenta, code_giro, valor_giro, password, caja, valores)# invoca a despliegue
  if  ejecutar == 'off':# Conecta con despliegue para apagar cajero
    print('APAGANDO...')
    print('HASTA PRONTO...')
    break