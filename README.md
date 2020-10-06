# IA_aplicada_a_la_solucion_de_laberintos
Implementación de algoritmos bio-inspirados para la solución de laberintos.

### Comenzando
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Pre-requisitos
Para poder replicar el proyecto en tu máquina local es necesario que tengas instalado el entorno de simulación CoppeliaSim, puedes descargarlo desde el siguiente enlace: https://www.coppeliarobotics.com/downloads.

Los algoritmos serán desarrollados utilizando el lenguaje Python, no importa la versión instalada, aunque se sugiere tener la versión 2.7 o superior para dotar a los algoritmos de caracteristicas futuras.

### Configuración
CoppeliaSim está diseñado para ser programado en LUA, sin embargo, los algoritmos a implementar están orientados en Python por lo que será necesario configurar nuestro entorno y generar un puerto de comunicación remota. Para ello, es necesario que los ficheros:
- sim.py
- simConst.py
- remoteApi.dll

se encuentren en la carpeta contenedora del código fuente pues serán estos quienes permitan crear la conexión.

Una vez efectuado el paso previo será necesario que se genere una nueva escena en el entorno de CoppeliaSim y se coloque dentro de ella el modelo del robot **Pioneer_p3dx**, se desactive el script por defecto y se genere un nuevo script del tipo **child script** el que será asopciado al modelo a manipular.
Dentro de ese script solo se deberá añadir de manera global la instrucción: 
> simRemoteApi.start(19999)

quien establece el puerto remopto a utilizar (este mismo puerto está asignado en la conexión del fichero *Maze_solver.py*)

### Ejecutando las pruebas
Para verificar que la conexion se realizó efectivamente, será necesario inicar primeramente la simulación desde el entorno CoppeliaSim y posteriormente ejecutar el script *Maze_solver.py*

### Contribuciones
Por favor lee el archivo CONTRIBUTING.md para detalles de contribución y el proceso de enviarnos pull request
