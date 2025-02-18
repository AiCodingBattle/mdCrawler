Django
The web framework for perfectionists with deadlines.
Cambiar tema (tema actual: automático)
Cambiar tema (tema actual: claro)
Cambiar tema (tema actual: oscuro)
Toggle Light / Dark / Auto color theme
Menu
  * Overview
  * Download
  * Documentation
  * News
  * Community
  * Code
  * Issues
  * About
  * ♥ Donate
  * Cambiar tema (tema actual: automático)
Cambiar tema (tema actual: claro)
Cambiar tema (tema actual: oscuro)
Toggle Light / Dark / Auto color theme


# Documentación
Search: Buscar
  * Getting Help


  * el
  * en
  * fr
  * id
  * it
  * ja
  * ko
  * pl
  * pt-br
  * zh-hans
  * Idioma: **es**


  * 1.10
  * 1.11
  * 2.0
  * 2.1
  * 2.2
  * 3.0
  * 3.1
  * 3.2
  * 4.0
  * 4.1
  * 4.2
  * 5.0
  * dev
  * Versión de la documentación: **5.1**


  * 

# Documentación de Django¶
Todo lo que necesita saber sobre Django.
## Los primeros pasos¶
¿Es usted nuevo en Django o con la programación? ¡Este es el lugar para comenzar!
  * **Desde cero:** Visión general | Instalación
  * **Tutorial:** Parte 1: Solicitudes y respuestas | Parte 2: Modelos y el sitio de administración | Parte 3: Vistas y plantillas | Parte 4: Formularios y vistas genéricas | Parte 5: Pruebas | Parte 6: Archivos estáticos | Parte 7: Personalización del sitio de administración | Parte 8: Agregar paquetes de terceros
  * **Tutoriales Avanzados:** :doc`Como escribir aplicaciones reutilizabes <intro/reusable-apps>` | Escriba su primera contribución para Django


## Obtener ayuda¶
¿Tiene algún problema? ¡Nos gustaría ayudar!
  * Prueba con las Preguntas Frecuentes – contienen las respuestas a muchas preguntas comunes.
  * ¿Buscando información específica? Intente con Índice, Índice de Módulos o la tabla de contenidos detallada.
  * ¿No ha encontrado nada? Mire FAQ: Obteniendo ayuda para información de como obtener soporte y hacer preguntas a la comunidad.
  * Reporte bugs con Django en nuestro rastreador de tickets.


## Como está organizada la documentación¶
Django tiene mucha documentación. Una descripción general de alto nivel de cómo se organiza le ayudará a saber dónde buscar ciertas cosas:
  * Los Tutoriales lo llevan de la mano a través de una serie de pasos para crear una aplicación web. Empiece aquí si es nuevo en Django o en el desarrollo de aplicaciones web. También mire»Los primeros pasos».
  * Guías temáticas discuten los temas y conceptos fundamentales en un nivel bastante alto y proporcionan información y explicación de antecedentes valiosa.
  * Guías de referencia contienen la referencia técnica para las APIs y otros aspectos del sistema de Django. Describen cómo funciona y cómo utilizarla, pero da por sentado que usted tiene un conocimiento básico de los conceptos claves.
  * Las guías de uso son fórmulas. Lo guian a través de los pasos involucrados en abordar los problemas principales y los casos de uso. Son más avanzadas que los tutoriales y dan por sentado el tener algo de conocimiento sobre cómo funciona Django.


## La capa del modelo¶
Django proporciona una capa de abstracción (los «modelos») para estructurar y manipular los datos de su aplicación web. Aprenda más sobre esta a continuación:
  * **Modelos:** Introducción a los modelos | Tipos de campos | Índices | Opciones Meta | Clase Model
  * **Querysets:** Haciendo consultas | Referencia de métodos de QuerySet | Expresiones de búsqueda
  * **Instancias de modelos:** Métodos de las instancias | Accediendo a objetos relacionados
  * **Migraciones:** Introducción a las migraciones | Referencia de operaciones | SchemaEditor | Escribiendo migraciones
  * **Avanzado** Administradores | SQL en bruto | Transacciones | Agregación | Búsqueda | Campos personalizados | Múltiples bases de datos | Búsquedas personalizadas | Expresiones de consulta | Expresiones condicionales | Funciones de Base de Datos
  * **Otros:** Bases de datos soportadas | Bases de datos heredadas | Proporcionando los datos iniciales | Optimizar el acceso a la base de datos | Características específicas de PostgreSQL


## La capa de vista¶
Django tiene el concepto de «vistas» para encapsular la lógica responsable de procesar una petición del usuario y devolver la respuesta. Encuentre todo lo que necesita saber sobre las vistas a través de los siguientes enlaces:
  * **Lo básico:** URLconfs | Funciones de vistas | Atajos | Decoradores | Soporte asíncrono
  * **Referencia:** Vistas incorporadas en Django | Objetos petición/respuesta | Objetos TemplateResponse
  * **Carga de archivos:** Visión general | Objetos de archivo | API de almacenamiento | Gestión de archivos | Almacenamiento personalizado
  * **Vistas basadas en clases:** Visión general | Vistas incorporadas para visualización | Vistas incorporadas para edición | Usando Mixins | Referencia de la API | Índice estático
  * **Avanzado:** Generación de archivos CSV | Generación de archivos PDF
  * **Middleware:** Visión general | Clases de Middleware incorporadas


## La capa de plantillas¶
La capa de plantillas provee una sintaxis amigable para los diseñadores que permite mostrar la información que se presentará al usuario. Aprenda cómo esta sintaxis puede ser usada por los diseñadores y extendida por los programadores:
  * **Lo básico:** Visión general
  * **Para los diseñadores:** Información general del lenguaje | Etiquetas y filtros incorporados | Humanización
  * **Para programadores:** API de plantilla | Etiquetas y filtros personalizados | Backend personalizado de plantilla


## Formularios¶
Django provee un poderoso framework para facilitar la creación de formularios y la manipulación de sus datos.
  * **Lo básico:** Visión general | API de formularios | Campos incorporados | Widgets incorporados
  * **Avanzado:** Formularios para modelos | Integración de medios | Conjuntos de formularios | Personalización de la validación


## El proceso de desarrollo¶
Aprenda sobre los diversos componentes y herramientas para ayudarse en el desarrollo y pruebas de aplicaciones Django:
  * **Ajustes:** Visión general | Lista completa de ajustes
  * **Aplicaciones:** Información general
  * **Excepciones:** Visión general
  * **django-admin y manage.py:** Información general | Añadiendo comandos personalizados
  * **Pruebas:** Introducción | Creación y ejecución de pruebas | Herramientas de pruebas incluidas | Temas avanzados
  * **Despliegue:** Resumen | Servidores WSGI | Servidores ASGI | Desplegando archivos estáticos | Seguimiento de errores del código mediante correo electrónico | Lista de verificación de despliegue


## El sitio administrativo¶
Encuentre todo lo que necesita saber acerca de la interfaz administrativa automatizada, una de las funcionalidades más populares de Django:
  * Sitio administrativo
  * Acciones del sitio administrativo
  * Generador de documentación del sitio administrativo


## Seguridad¶
La seguridad es un tema de suma importancia en el desarrollo de aplicaciones web y Django provee múltiples herramientas y mecanismos de protección:
  * Información general de la seguridad
  * Problemas de seguridad en Django revelados
  * Protección contra clickjacking
  * Protección de Falsificación de Petición entre Sitios
  * Firma criptográfica
  * Middleware de seguridad


## Internacionalización y localización¶
Django ofrece un robusto framework de internacionalización y localización para ayudarle en el desarrollo de aplicaciones para múltiples idiomas y regiones del mundo:
  * Información general | Internacionalización | Localización | Formato localizado de la interfaz web y entrada de formulario
  * Husos horarios


## Rendimiento y optimización¶
Existe una variedad de técnicas y herramientas que lo pueden ayudar a ejecutar el código de forma más eficiente y rápida y con menos uso de recursos del sistema.
  * Visión general sobre rendimiento y optimización


## Framework geográfico¶
GeoDjango tiene como propósito ser un framework para el desarrollo geográfico de clase mundial. Su meta es hacer lo más fácil posible construir aplicaciones web GIS y aprovechar el poder de los datos habilitados de forma espacial.
## Herramientas comunes para aplicaciones web¶
Django ofrece múltiples herramientas que son necesarias para el desarrollo de aplicaciones web:
  * **Autenticación:** Información general | Usando el sistema de autenticación | Gestión de contraseñas | Personalizando la autenticación | Referencia de la API
  * Almacenamiento en caché
  * Registro
  * Enviando correos
  * Fuentes de redifusión (RSS/Atom)
  * Paginación
  * Framework de mensajes
  * Serialización
  * Sesiones
  * Mapas de sitio
  * Gestión de archivos estáticos
  * Validación de datos


## Otras funcionalidades básicas¶
Aprenda sobre otras funcionalidades básicas del framework Django:
  * Procesamiento condicional de contenido
  * Tipos de contenido y relaciones genéricas
  * Páginas estáticas
  * Redirecciones
  * Señales
  * Framework de comprobación de sistema
  * El framework de sitios
  * Unicode en Django


## El proyecto de código abierto Django¶
Aprenda sobre el proceso de desarrollo para el proyecto Django en sí y sobre cómo puede contribuir:
  * **Community:** Contributing to Django | The release process | Team organization | The Django source code repository | Security policies | Mailing lists and Forum
  * **Filosofías de diseño:** Información general
  * **Documentación:** Sobre esta documentación
  * **Distribuciones de terceros:** Visión general
  * **Django en el tiempo:** Estabilidad de la API | Notas de versión e instrucciones de actualización | Linea de tiempo de funcionalidades en desuso


Contenidos de la documentación de Django
Empezando 
Back to Top
# Información Adicional
## Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * Hale Law, P.A. donated to the Django Software Foundation to support Django development. Donate today! 


## Mostrar
  * Previo: Contenidos de la documentación de Django
  * Siguiente: Empezando
  * Tabla de contenidos
  * Índice General
  * Índice de Módulos Python


## Está aquí:
  * Documentación de Django 5.1 
    * Documentación de Django


## Obtener ayuda
FAQ
    Pruebe las preguntas frecuentes: tiene respuestas a muchas preguntas comunes.
Índice, Índice del módulo, or Tabla de Contenidos
    Práctico cuando se busca información específica.
Django Discord Server
    Join the Django Discord Community.
Official Django Forum
    Join the community on the Django Forum.
Ticket tracker
    Reporte bugs con Django o con la documentación de Django en nuestro rastreador de tickets.
## Descarga:
Desconectado (Django 5.1): HTML | PDF | ePub Proporcionado por Lea los documentos. 
# Django Links
## Learn More
  * About Django
  * Getting Started with Django
  * Team Organization
  * Django Software Foundation
  * Code of Conduct
  * Diversity Statement


## Get Involved
  * Join a Group
  * Contribute to Django
  * Submit a Bug
  * Report a Security Issue
  * Individual membership


## Get Help
  * Getting Help FAQ
  * Django Discord
  * Official Django Forum


## Follow Us
  * GitHub
  * Twitter
  * Fediverse (Mastodon)
  * News RSS


## Support Us
  * Sponsor Django
  * Corporate membership
  * Official merchandise store
  * Benevity Workplace Giving Program


Django
  * Hosting by In-kind donors
  * Design by Threespot & andrevv


© 2005-2025  Django Software Foundation and individual contributors. Django is a registered trademark of the Django Software Foundation. 
