# BotBuzz

BotBuzz es un módulo de Python diseñado para facilitar el envío de mensajes y notificaciones a través de un bot de Telegram. Este módulo permite integrar de manera sencilla la funcionalidad de mensajería de Telegram en tus aplicaciones, usando el token de tu bot.

## Instalación

Para instalar BotBuzz, puedes clonar el repositorio y luego instalarlo usando pip en tu ambiente virtual:

```bash
git clone https://github.com/IamRodion/BotBuzz.git
cd BotBuzz
pip install . # Con el ambiente virtual activado
```

O puedes descargar la [última versión](https://github.com/IamRodion/BotBuzz/releases) en vez de clonar el repo.

## Uso

A continuación, se presentan ejemplos de cómo utilizar el módulo BotBuzz para enviar mensajes, enviar stickers y leer mensajes de un usuario de Telegram.

### Enviar un Mensaje

Para enviar un mensaje a un usuario de Telegram, primero necesitas crear una instancia de `Bot` y `Contact`. Luego, puedes usar el método `send_message` del bot.

```python
from BotBuzz import Bot, Contact

# Configura el token de tu bot y el nombre
TOKEN = 'TU_TOKEN_DE_TELEGRAM'
bot = Bot(TOKEN=TOKEN, name="Mi Bot")

# Crea un contacto con el nombre y el chat_id del usuario
contacto = Contact(name="Usuario", chat_id=123456789)

# Envía un mensaje al contacto
bot.send_message(contact=contacto, text="Hola, este es un mensaje de prueba!")
```

### Enviar un Sticker

Para enviar un sticker, utiliza el método `send_sticker` del bot, proporcionando el ID del sticker que deseas enviar.

```python
from BotBuzz import Bot, Contact

TOKEN = 'TU_TOKEN_DE_TELEGRAM'
bot = Bot(TOKEN=TOKEN, name="Mi Bot")

contacto = Contact(name="Usuario", chat_id=123456789)

# Envía un sticker al contacto
bot.send_sticker(contact=contacto, sticker="CAACAgIAAxkBAAEwo3xnfh0dgWfPOjBubK4DIm8awlWQlwACvAwAAocoMEntN5GZWCFoBDYE")
```

### Leer Mensajes

Para leer mensajes de un usuario específico, utiliza el método `read_message`. Este método devuelve una lista de mensajes recibidos.

```python
from BotBuzz import Bot, Contact

TOKEN = 'TU_TOKEN_DE_TELEGRAM'
bot = Bot(TOKEN=TOKEN, name="Mi Bot")

contacto = Contact(name="Usuario", chat_id=123456789)

# Lee los mensajes del contacto
mensajes = bot.read_message(contact=contacto)
for mensaje in mensajes:
    print(mensaje)
```
