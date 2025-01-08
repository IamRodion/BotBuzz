class Contact:
    """Contacto del usuario de telegram
    Atributos:
        name: El nombre con el que se le debe llamar al contacto en formato string
        chat_id: El id del chat entre el contacto y el bot"""
    def __init__(self, name: str, chat_id: int):
        self.name = name
        self.chat_id = chat_id

    def __str__(self) -> str:
        return f'Objeto Contact: {self.name}'