#RaspBy-Car
	
*Móvil pequeño que funcionará gracias Raspberry y OpenCV para poder seguir un determinado color, además de poder ser controlado por Smartphones.*

<IMG SRC=http://blog.todoelectronica.com/wp-content/uploads/2012/05/tracking-arduino-1.jpg WIDTH=200 HEIGTH=100 ALIGN=RIGHT />

##Contenidos del Proyecto
1. [Consideraciones](#consideraciones)
2. [Funcionamiento](#funcionamiento)
3. [Requisitos](#requisitos)
4. [Referencias](#referencias)

##Consideraciones:
	

- RaspBy-Car será un pequeño móvil dotado de todas las necesidades básicas de un automóvil controlado a distancia mediante un Smartphone, pero que, a la vez, contará con una webcam funcionando con OpenCV para detectar colores y que el móvil los siga.
- Buscamos un método de detección rápido y que sea simple para el usuario. Del modelo físico, agilidad y poco peso, para que no requiera mayor gasto de energía.
- Este móvil tendría la capacidad de seguir un camino de colores. Esto le permitiría transportar cargas pequeñas. Además, gracias a que podrá ser controlado mediante un Smartphone, podría facilitar el trabajo en  caso que se necesite el desvío del camino.




##Funcionamiento:


- El móvil contará con un eje rotatorio, y una estructura que permitirá mantenerlo recto. Cada rueda será movida de manera independiente, tal que el auto pueda girar 360° con facilidad y seguir un color de manera simple.
- Las ruedas serán controladas por Raspberry, que enviará las respuestas producto de OnpenCV, a los motores que permitirán el movimiento que las ruedas necesitan.
- Se estudia la posibilidad de agregar otro movimiento a la cámara: Vertical, para hallar colores que estén sobre el móvil.
- Para evitar que el móvil choque con algún objeto, contará con sensores de profundidad (Aún en estudio).

##Requisitos:


- Raspberry
 
- Botones

- Web-Cam

- Motores DC

- Materiales livianos para estructura, correspondiente a utlización de impresion 3d

- Baterías

- Sensores de Profundidad
	

##Referencias:

 
 - Cámara Rastreadora de colores: http://blog.todoelectronica.com/2012/05/boston/
 

 - Pan tracking webcam using OpenCV and Arduino': https://www.youtube.com/watch?v=Gg6zqjDq1ho


 - Auto controlado por Wi-Fi y hecho con Arduino: http://www.blairkelly.ca/arduino-wifly-mini#awm-moc
