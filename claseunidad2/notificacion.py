from abc import ABC, abstractmethod

# Interfaz (clase abstracta) para notificaciones
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
        

if __name__ == "__main__":
    sms = NotificacionSMS(f"Hola, bro que haces?", "+573001112233")
    email = NotificacionEmail(f"Hola, bro que haces?", "usuario@correo.com")
    sms.enviar()
    email.enviar()
    
