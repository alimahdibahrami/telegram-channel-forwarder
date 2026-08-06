

# Reenviador de Canales de Telegram

Un script en Python que reenvía mensajes de un canal de Telegram a otro utilizando la biblioteca Telethon. Este script es compatible con mensajes de texto y multimedia, y mantiene un registro del último mensaje reenviado para evitar duplicados.

## Características

- **Reenvío de mensajes de texto y multimedia**: Reenvía mensajes de texto y multimedia desde un canal de origen hacia un canal de destino.
- **Seguimiento del último mensaje enviado**: Mantiene un registro del último mensaje enviado para evitar reenvíos duplicados.
- **Sesión persistente de Telegram**: La sesión se guarda localmente, por lo que no necesitas volver a ingresar el código de inicio de sesión cada vez que ejecutes el script. Esto evita que Telegram te bloquee temporalmente por exceso de solicitudes de inicio de sesión.
- **Reanudación desde el último mensaje enviado**: Si el programa se detiene por cualquier motivo (por ejemplo, problemas de internet), puede reanudarse desde el último mensaje enviado tras reiniciarse.
- **Retraso aleatorio entre mensajes**: Incluye un retraso aleatorio entre mensajes para evitar ser marcado por Telegram.

## Requisitos previos

- Python 3.7 o superior
- Biblioteca Telethon

## Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/yourusername/telegram-channel-forwarder.git
   cd telegram-channel-forwarder
   ```

2. **Instalar Dependencias**

   Instala las bibliotecas de Python requeridas usando pip:

   ```bash
   pip install telethon
   ```

## Primeros Pasos

1. **Obtener Credenciales de API de Telegram**

   Para usar este script, necesitas obtener tu `api_id` y `api_hash` desde las [Herramientas de Desarrollo de API de Telegram](https://my.telegram.org/apps).

2. **Configurar el Script**

   Abre el archivo `script.py` y completa las siguientes variables:

   ```python
   api_id = 'YOUR_API_ID'
   api_hash = 'YOUR_API_HASH'
   phone_number = '+YOUR_PHONE_NUMBER'
   session_name = 'YOUR_SESSION_NAME'
   source_channel_id = 'SOURCE_CHANNEL_ID'
   destination_channel_id = 'DESTINATION_CHANNEL_ID'
   ```

3. **Ejecutar el Script**

   Ejecuta el script con Python:

   ```bash
   python script.py
   ```

   El script solicitará un código de inicio de sesión enviado a tu aplicación de Telegram si es la primera vez que lo ejecutas. Ingresa el código para autenticarte.

## Cómo Funciona

- El script se conecta al cliente de Telegram utilizando las credenciales proporcionadas.
- Obtiene los mensajes del canal de origen especificado y los reenvía al canal de destino.
- Se utiliza un archivo JSON (`last_message.json`) para mantener un registro del último mensaje enviado, garantizando que ningún mensaje se envíe dos veces.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](https://github.com/alimahdibahrami/telegram-channel-forwarder/blob/main/LICENSE) para obtener más detalles.
