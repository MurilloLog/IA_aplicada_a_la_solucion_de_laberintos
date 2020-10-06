''' Maze Solver utilizando IA '''
# Script de conexion a CoppeliaSim
# En este script se presenta el codigo necesario para 
# crear un puerto de comunicacion entre el lenguaje Python
# y el entorno de simulacion CoppeliaSim.
# Para poder ejercutarse correctamente deberan estar presentes
# dentro del mismo directorio del script los ficheros: 
# - RemoteApi.dll
# - sim.py
# - simConst.py
#
# Una vez cumplido el requisito previo debera crear un child-script
# desde CoppeliaSim y enlazarlo a cualquier objeto de la escena a
# trabajar para poder agregar la siguiente instruccion:
#
#      simRemoteApi.start(19999)
#

############## CONEXION ############## 
try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" no pudo ser importada. Esto significa que probablemente')
    print ('"sim.py" o la libreria de acceso remoto no pudo ser encontrada.')
    print ('Asegurese de que ambas librerias se encuentran en el mismo directorio,')
    print ('o ajusta apropiadamente el fichero "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')
import sys
import time

sim.simxFinish(-1) # Cerrar todas las conexiones abiertas
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Configurando los parametros de comunicacion
if clientID!=-1:
    print ('Conectado a un servidor API remoto')
else:
    print ('Conexion no exitosa')
    sys.exit('No se pudo conectar')
############################


