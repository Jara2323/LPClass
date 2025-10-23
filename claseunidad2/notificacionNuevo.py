from abc import ABC, abstractmethod

class Notificacion(ABC):
    def __init__(self, mensaje: str, destinatario: str):
        self.mensaje = mensaje
        self.destinatario = destinatario

    @abstractmethod
    def enviar(self):
        pass

class NotificacionSMS(Notificacion):
    def enviar(self):
        print(f"Enviando SMS a {self.destinatario}: {self.mensaje}")

class NotificacionEmail(Notificacion):
    def enviar(self):
        print(f"Enviando Email a {self.destinatario}: {self.mensaje}")

class WhatsAppAPI:
    def send_msg(self, phone, text):
        print(f"[WhatsApp] Mensaje enviado a {phone}: {text}")

class NotificacionWhatsAppAdapter(Notificacion):
    def __init__(self, mensaje: str, destinatario: str, api: WhatsAppAPI):
        super().__init__(mensaje, destinatario)
        self.api = api

    def enviar(self):
        self.api.send_msg(self.destinatario, self.mensaje)

class GestorNotificaciones:
    def __init__(self, notificacion: Notificacion):
        self.notificacion = notificacion

    def enviar(self):
        self.notificacion.enviar()

if __name__ == "__main__":
    sms = NotificacionSMS("Hola, bro que haces?", "+573001112233")
    email = NotificacionEmail("Revisa tu correo, por favor", "usuario@correo.com")
    whatsapp_api = WhatsAppAPI()
    whatsapp = NotificacionWhatsAppAdapter("Ey bro que haces?, deberias de prestar atencion!", "+573009998877", whatsapp_api)

    gestor1 = GestorNotificaciones(sms)
    gestor1.enviar()

    gestor2 = GestorNotificaciones(email)
    gestor2.enviar()

    gestor3 = GestorNotificaciones(whatsapp)
    gestor3.enviar()