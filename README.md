# Tutorial de Reportes a través de Chatbot 

# Sobre RapidPro y Textit

RapidPro es un proyecto creado por UNICEF y es completamente de código abierto. Para efectos prácticos, utilizamos un hosting de este proyecto llamado TextIt, pero puedes crear toda la plataforma de trabajo enteramente desde cero utilizando el código abierto. Todos los detalles y el código fuente del proyecto RapidPro se pueden encontrar en su repositorio de GitHub: [https://github.com/rapidpro/rapidpro](https://github.com/rapidpro/rapidpro)


# Flujos a TextIt o RapidPro

La lógica de interacción está diseñada en flujos, estos flujos contienen las interacciones con los usuarios, esta interacción es posible realizarla en diferentes canales, la versión del proyecto TUMI CAF está configurada para trabajar en WhatsApp, puede acceder [aquí](https://api.whatsapp.com/send?phone=573114661292&text=Hola)

La lógica de interacción puede ser usada también en Telegram, además de WhatsApp.

Este repositorio contiene flujos exportados en formato JSON para ser utilizados en TextIt o cualquier proyecto basado en la plataforma RapidPro. A continuación, encontrarás una guía paso a paso para importar estos flujos a tu instancia de TextIt o RapidPro.

## Requisitos

Antes de comenzar, asegúrate de tener lo siguiente:

1. Una cuenta en [TextIt](https://textit.in/) o en una instancia de [RapidPro](https://rapidpro.io/).
2. Acceso al editor de flujos en la plataforma.
3. El archivo JSON que contiene los flujos exportados de este repositorio.

## Pasos para importar flujos

1. Inicia sesión en tu cuenta de TextIt o RapidPro.
2. Ve al editor de flujos haciendo clic en el menú "Flujos" en la parte superior de la página.
3. Haz clic en el botón "Importar" en la esquina superior derecha.
4. Selecciona el archivo JSON que contiene los flujos exportados de este repositorio.
5. Confirma la importación haciendo clic en "Importar" en la ventana emergente.
6. Espera a que la plataforma importe los flujos y luego aparecerán en la lista de flujos disponibles.
7. Puedes encontrar más información de como hacer esto en la plataforma en TextIt [aquí](https://help.textit.com/en/article/importing-a-flow-cmfox6/)

## Personalizar flujos

Una vez importados los flujos, es posible que necesites personalizarlos según tus necesidades. Para hacerlo, sigue estos pasos:

1. Haz clic en el flujo que deseas editar en la lista de flujos disponibles.
2. Realiza las modificaciones necesarias utilizando el editor de flujos.
3. Guarda tus cambios haciendo clic en el botón "Guardar" en la esquina superior derecha.
4. Si es necesario, repite estos pasos para cada flujo que desees personalizar.

## Notas adicionales

- Asegúrate de conectar correctamente los flujos importados a tus canales de comunicación (por ejemplo, números de teléfono, cuentas de redes sociales, etc.).
- Verifica que las palabras clave, etiquetas y otras configuraciones específicas del flujo sean las adecuadas para tu caso de uso.
- No olvides probar tus flujos antes de usarlos en un entorno de producción.

## Soporte

Si tienes alguna pregunta o necesitas ayuda, no dudes en abrir un [issue](https://github.com/tu_usuario/tu_repositorio/issues) en este repositorio.

# Crear una copia de la base de datos Airtable

Este proyecto utiliza una base de datos Airtable como parte de su infraestructura. Para replicar la base de datos en tu propia cuenta de Airtable, sigue los pasos a continuación:

## Paso 1: Crear una cuenta en Airtable

Si aún no tienes una cuenta en Airtable, sigue estos pasos para crear una:

1. Ve a [Airtable.com](https://airtable.com/).
2. Haz clic en "Registrarse" en la parte superior derecha de la pantalla.
3. Puedes registrarte con tu dirección de correo electrónico o utilizando una cuenta de Google, Apple o Microsoft. Sigue las instrucciones en pantalla para completar el proceso de registro.

## Paso 2: Acceder al enlace del template

Haz clic en el siguiente enlace para acceder al template de la base de datos Airtable que se utilizará en este proyecto:

[Template de Airtable](https://airtable.com/shrPOBl3obHbRe4i5)

## Paso 3: Copiar el template a tu cuenta de Airtable

1. Una vez que hayas accedido al enlace del template, verás una vista previa de la base de datos.
2. Haz clic en el botón "Usar plantilla" en la esquina superior derecha.
3. En la ventana emergente, elige un nombre para la base de datos y selecciona el espacio de trabajo en el que deseas crearla.
4. Haz clic en "Usar plantilla" para crear una copia de la base de datos en tu cuenta de Airtable.

## Paso 4: Personalizar la base de datos (opcional)

Una vez que hayas creado la copia de la base de datos, puedes personalizarla según tus necesidades. Para hacerlo, sigue estos pasos:

1. Abre la base de datos que acabas de crear en tu cuenta de Airtable.
2. Personaliza los campos, vistas y configuraciones según tus necesidades.
3. No olvides guardar los cambios realizados en la base de datos.

## Paso 5: Conectar la base de datos a tu proyecto

Después de replicar y personalizar la base de datos, necesitarás conectarla a tu proyecto. Consulta la documentación de Airtable API y la biblioteca que estés utilizando en tu proyecto (por ejemplo, airtable.js, Airtable.py, etc.) para obtener instrucciones sobre cómo hacerlo.

## Soporte

Si tienes alguna pregunta o necesitas ayuda, no dudes en abrir un [issue](https://github.com/tu_usuario/tu_repositorio/issues) en este repositorio.


# Configurar la API key de Airtable en TextIt/RapidPro

Este proyecto utiliza la API de Airtable para interactuar con la base de datos. Para configurar la API key en TextIt/RapidPro, sigue los pasos a continuación:

## Paso 1: Obtener la API key de Airtable

1. Inicia sesión en tu cuenta de [Airtable](https://airtable.com/).
2. Haz clic en tu imagen de perfil en la esquina superior derecha y selecciona "Cuenta".
3. En la sección "API key", verás tu clave de API personal. Si no tienes una clave de API, haz clic en "Generar clave de API" para crear una.
4. Copia la clave de API generada (por ejemplo, `keyXXXXXXXXX`).

**Nota:** Mantén tu API key en secreto, ya que permite el acceso a tus bases de datos en Airtable.

## Paso 2: Crear una variable global en TextIt/RapidPro

1. Inicia sesión en tu cuenta de TextIt o RapidPro.
2. Ve a la página de "Variables Globales" haciendo clic en el menú "Cuentas" en la parte superior de la página y luego selecciona "Variables Globales".
3. Haz clic en el botón "Crear" en la esquina superior derecha.
4. Introduce un nombre para la variable global, debe tener el nombre, `apikey`.
5. En el campo "Valor", pega la clave de API de Airtable que copiaste en el Paso 1, asegurándote de agregar el prefijo "Bearer " antes de la clave de API (por ejemplo, `Bearer keyXXXXXXXXX`).
6. Haz clic en "Crear" para guardar la variable global.

Los flujos en este proyecto ya están preconfigurados para usar la variable `@globals.apikey` en las llamadas a la API de Airtable. Con la variable global configurada, tus flujos deberían funcionar correctamente con la base de datos de Airtable.

# Uso del canal de WhatsApp en nuestro proyecto

Nuestro proyecto se basa en el canal de WhatsApp para la comunicación. Para acceder a la API de WhatsApp, utilizamos una plataforma intermediaria llamada [360dialog.com](https://www.360dialog.com/). Sin embargo, es posible hacer la conexión con otros operadores como [Twilio](https://www.twilio.com/whatsapp).

## Creación de una cuenta en 360dialog y configuración de Facebook Business

Para utilizar el canal de WhatsApp a través de 360dialog, es necesario crear una cuenta y configurar Facebook Business. A continuación, se presentan los pasos generales para hacerlo:

1. Ve al sitio web de [360dialog](https://www.360dialog.com/) y crea una cuenta siguiendo las instrucciones en pantalla.

2. Una vez que hayas creado una cuenta en 360dialog, debes vincularla a Facebook Business. Para ello, sigue los pasos proporcionados por 360dialog en su [documentación oficial](https://docs.360dialog.com/).

3. Asegúrate de tener una cuenta de [Facebook Business](https://business.facebook.com/) y de seguir las instrucciones para configurarla correctamente. Esto incluye la creación y configuración de una página de empresa y la vinculación de la cuenta de 360dialog a tu cuenta de Facebook Business.

4. Durante el proceso de configuración de Facebook Business, es necesario registrar el número de teléfono que se utilizará para el canal de WhatsApp. Facebook puede solicitar información adicional sobre tu empresa, como datos de contacto y documentación que respalde la verificación de la información proporcionada.

5. Facebook revisará la información proporcionada y, una vez aprobada, podrás utilizar el número de teléfono registrado en tu proyecto de TextIt/RapidPro a través de la plataforma 360dialog.

**Nota:** El proceso de revisión y verificación de la información de tu empresa por parte de Facebook puede llevar tiempo. Por lo tanto, es importante comenzar este proceso con suficiente anticipación para evitar retrasos en la implementación de tu proyecto.



## Soporte

Si tienes alguna pregunta o necesitas ayuda, no dudes en abrir un [issue](https://github.com/tu_usuario/tu_repositorio/issues) en este repositorio.
