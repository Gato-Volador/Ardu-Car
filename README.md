#Ardu-Car
	
*Móvil pequeño que funcionará gracias a placas Arduino y OpenCV para poder seguir un determinado color, además de poder ser controlado por Smartphones.*

<IMG SRC=http://blog.todoelectronica.com/wp-content/uploads/2012/05/tracking-arduino-1.jpg WIDTH=200 HEIGTH=100 ALIGN=RIGHT />

##Contenidos del Proyecto
1. [Consideraciones](#consideraciones)
2. [Funcionamiento](#funcionamiento)
3. [Requisitos](#requisitos)
4. [Referencias](#referencias)

##Consideraciones:
	

- Ardu-Car será un pequeño móvil dotado de todas las necesidades básicas de un automóvil controlado a distancia mediante un Smartphone, pero que, a la vez, contará con una webcam funcionando con OpenCV para detectar colores y que el móvil los siga.
- Buscamos un método de detección rápido y que sea simple para el usuario. Del modelo físico, agilidad y poco peso, para que no requiera mayor gasto de energía.
- Este móvil tendría la capacidad de seguir un camino de colores. Esto le permitiría transportar cargas pequeñas. Además, gracias a que podrá ser controlado mediante un Smartphone, podría facilitar el trabajo en  caso que se necesite el desvío del camino.




##Funcionamiento:


- El móvil contará con dos ejes rotatorios para las ruedas, que serán movidos gracias a la acción de un pequeño motor que funcionará como respuesta al programa, ya sea aercándose o alejandose del objetivo.
- También se contará con un servomotor que permitirá acomodar el sentido y la dirección del móvil, para mantener el color a seguir siempre al frente de la cámara.
- En caso de que el aparato necesite buscar un color o el servomotor de la dirección no permite orientar la cámara hacia el color (ya sea porque hay un pared que impide al móvil orientarse bien o hay un espacio reducido), se agregará otro servomotor a la base de la cámara que le permitirá girar de forma paralela al suelo. 
- Se estudia la posibilidad de agregar otro movimiento a la cámara: Vertical, para hallar colores que estén sobre el móvil.
- Para evitar que el móvil choque con algún objeto, contará con sensores de profundidad.

##Requisitos:


- Placas Arduino
 
- Motor

- Web-Cam

- Servomotores

- Materiales livianos para estructura, correspondiente a utlización de impresion 3d

- Baterías

- Sensores de Profundidad
	

##Referencias:

 
 - Cámara Rastreadora de colores: http://blog.todoelectronica.com/2012/05/boston/
 

 - Pan tracking webcam using OpenCV and Arduino': https://www.youtube.com/watch?v=Gg6zqjDq1ho


 - Auto controlado por Wi-Fi y hecho con Arduino: http://www.blairkelly.ca/arduino-wifly-mini#awm-moc
