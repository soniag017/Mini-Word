# Mini-Word

Editor de texto desarrollado en Python utilizando PySide6. Proporciona funcionalidades básicas y avanzadas de edición, formateo y búsqueda de texto en un entorno sencillo y organizado.
La aplicación ha sido ampliada con nuevas características como reconocimiento por voz, generador de instaladores y firma digital del ejecutable.

Funcionalidades

Edición de texto

El editor ofrece todas las funciones esenciales para trabajar con texto:

Crear un documento nuevo.

Abrir archivos de texto (.txt).

Guardar el documento actual.

Copiar, cortar y pegar texto.

Deshacer y rehacer cambios.

Contador dinámico del número de palabras.

Formato de texto

El panel superior del editor permite aplicar distintos estilos de formato:

Activar y desactivar negrita.

Activar y desactivar cursiva.

Cambiar el tipo de fuente mediante un selector con todas las familias disponibles en el sistema.

Modificar el tamaño de la fuente, con valores predefinidos o personalizados.

Aplicar diferentes colores al texto.

Cambiar el color de fondo del área de edición.

Búsqueda y reemplazo

El editor incluye un panel de búsqueda avanzado que permite:

Buscar la siguiente coincidencia de un término.

Buscar la coincidencia anterior.

Mostrar el número total de coincidencias encontradas.

Reemplazar la coincidencia actual.

Reemplazar todas las apariciones del término buscado en el documento.

Gestión visual y diseño

El área de texto se adapta automáticamente al tamaño de la ventana, manteniendo proporción similar a un documento tipo A4.

Se utilizan iconos personalizados para todas las acciones del menú y la barra de herramientas.

El editor incorpora una barra de estado para mostrar mensajes informativos y el contador de palabras.

Reconocimiento por voz

El editor permite dictar texto mediante el micrófono gracias a la integración de SpeechRecognition. El texto reconocido se inserta automáticamente en el área de edición.
Para utilizar esta función es necesario instalar las dependencias correspondientes:

pip install SpeechRecognition
pip install pyaudio

Instalador con Inno Setup

El proyecto incluye un instalador generado con Inno Setup, permitiendo distribuir Mini-Word como una aplicación instalable en Windows. El instalador crea accesos directos, incluye iconos personalizados y facilita una instalación guiada para el usuario final.

Firma digital del ejecutable

El ejecutable generado con PyInstaller puede ser firmado digitalmente utilizando Signtool, proporcionando mayor seguridad y evitando advertencias de Windows.
Ejemplo de comando de firma utilizado:

signtool sign /f Certificado.pfx /p contraseña /fd SHA256 /tr http://timestamp.digicert.com
 /td SHA256 MiniWord.exe

Distribución

El repositorio contiene:
– Código fuente de la aplicación
– Versión portable generada con PyInstaller
– Instalador de la aplicación
– Archivos necesarios para la firma y empaquetado


<img width="789" height="626" alt="image" src="https://github.com/user-attachments/assets/abcc97b9-1d4b-4a34-9e33-492bad632987" />


<img width="602" height="432" alt="image" src="https://github.com/user-attachments/assets/1e56b93e-a54f-4eb9-a85e-5345eacffd2f" />



<img width="602" height="221" alt="image" src="https://github.com/user-attachments/assets/453715e8-7a11-4da5-8a19-318087028cdc" />

















