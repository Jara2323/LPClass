class UserSession():
    _instance_ = None

    def __init__(self):
        raise RuntimeError("Use login() method instead")

    @classmethod
    def login(cls, username=None, password=None):
        if cls._instance_ is None:
            cls._instance_ = cls.__new__(cls)
        # Simulación de autenticación
        if username == "juan" and password == "equisde123":
            cls._instance_.username = username
            cls._instance_.authenticated = True
        else:
            cls._instance_.username = None
            cls._instance_.authenticated = False
        return cls._instance_

    @classmethod
    def logout(cls):
        if cls._instance_ is not None:
            cls._instance_.username = None
            cls._instance_.authenticated = False

    def is_authenticated(self):
        return self.authenticated

    def get_user(self):
        return self.username

# Ejemplo de uso:
if __name__ == "__main__":
    sesion = UserSession.login("juan", "equisde123")
    print("¿Sesión autenticada?", sesion.is_authenticated()) 
    print("Usuario:", sesion.get_user())

    sesion2 = UserSession.login("otro", "equisde123")
    print("¿Sesión autenticada con datos incorrectos?", sesion2.is_authenticated()) 
    print("¿Es la misma instancia?", sesion is sesion2)  

    UserSession.logout()
    print("¿Sesión autenticada después de logout?", sesion.is_authenticated())  
    print("Usuario después de logout:", sesion.get_user())