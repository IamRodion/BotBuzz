import requests, logging
from typing import Callable, Dict, List, Optional
from .contact import Contact

class Bot:
    """Un bot de telegram

    Atributos:
        TOKEN: El token del bot que quieres usar, en formato string
        name: Nombre del bot en formato string
    """

    def __init__(self, TOKEN: str, name: str):
        self.TOKEN = TOKEN
        self.name = name

    def __str__(self) -> str:
        return f'Objeto Bot: {self.name}'
    
    def action(self, ACTION_NAME: str, REQUESTS_METHOD: Callable, payload: Dict = None) -> Optional[Dict]:
        """Realiza una acción sobre la API de telegram

        Args:
            ACTION_NAME: Nombre del endpoint en formato string
            REQUESTS_METHOD: Una función del módulo requests (requests.get o requests.post)
            payload: Datos a enviar en la solicitud, en formato dict

        Returns:
            Objeto json con la respuesta de la solicitud o None si falla
        """
        if payload is None:
            payload = {}
        URL = f'https://api.telegram.org/bot{self.TOKEN}/{ACTION_NAME}'
        try:
            response = REQUESTS_METHOD(URL, data=payload)
            if response.status_code == 200:
                print("Se realizó la acción correctamente")
                return response.json()
            else:
                print("No se pudo realizar la acción")
        except requests.RequestException as e:
            print(f"No se pudo enviar la solicitud: {e}")
        return None

    def send_message(self, contact: 'Contact', text: str):
        """Envía un texto al usuario de Telegram indicado

        Args:
            contact: Un objeto de tipo contacto que tiene los datos del usuario
            text: Un string a enviar

        Returns:
            None
        """
        payload = {
            'chat_id': contact.chat_id,
            'text': text
        }
        self.action(ACTION_NAME='sendMessage', REQUESTS_METHOD=requests.post, payload=payload)

    def send_sticker(self, contact: 'Contact', sticker: str):
        """Envía un sticker al usuario de Telegram indicado

        Args:
            contact: Un objeto de tipo contacto que tiene los datos del usuario
            sticker: Un string con el id del sticker

        Returns:
            None
        """
        payload = {
            'chat_id': contact.chat_id,
            'sticker': sticker
        }
        self.action(ACTION_NAME='sendSticker', REQUESTS_METHOD=requests.post, payload=payload)

    def read_message(self, contact: 'Contact') -> List[str]:
        """Muestra los mensajes recibidos desde un usuario de Telegram indicado

        Args:
            contact: Un objeto de tipo contacto que tiene los datos del usuario

        Returns:
            Lista de strings con los mensajes encontrados
        """
        data = self.action(ACTION_NAME='getUpdates', REQUESTS_METHOD=requests.get)
        messages = []
        if data:
            for result in data.get("result", []):
                message = result.get("message")
                if message and message["chat"]["id"] == contact.chat_id:
                    print(message["text"])
                    messages.append(message["text"])
        return messages