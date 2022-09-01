# ProyectosIoT
Proyectos de instrumentación electrónica en IoT

BOMBA DE INFUSION O JERINGA:
Se implementa un proyecto IoT que desarrolla tanto la parte de software como de hardware comunicandose entre sí por medio de una base de datos en la nube 
a través de internet. 
La primera etapa involucra el diseño del aplicativo web utilizando lenguaje Java, CCS HTML, con la finalidad de enviar la ejecucion de los comandos a la base 
de datos Google Firebase, en la cual se almacenan como variable. A su vez,en la segunda etapa se elabora e implementa la estructura mecanica 3D que da soporte a
la bomba de jeringa, que es controlada por motor bipolar CDROM a través de un L298N Puente H asociado a un microprocesador Raspberry Pi 4, el cual recoje las
variables almacenadas en la nube y ejecuta las órdenes a tiempo real.

Link del aplicativo web de control remoto: https://iot-bombadejeringa.web.app/
