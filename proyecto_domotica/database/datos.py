class BaseDatos:

    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializar()
        return cls._instancia

    def _inicializar(self):
        self.dispositivos = {
            'luces': [
                {'id': 1, 'nombre': 'Luz Sala', 'encendida': False, 'agente': 1},
                {'id': 2, 'nombre': 'Luz Cocina', 'encendida': True, 'agente': 2},
                {'id': 3, 'nombre': 'Luz Habitacion', 'encendida': False, 'agente': 3}
            ],
            'termostatos': [
                {'id': 1, 'nombre': 'Termo Sala', 'temperatura': 22.0, 'objetivo': 24.0, 'agente': 1},
                {'id': 2, 'nombre': 'Termo Habitacion', 'temperatura': 19.0, 'objetivo': 22.0, 'agente': 2}
            ],
            'contenedores': [
                {'id': 1, 'nombre': 'Contenedor Cocina', 'nivel': 75, 'agente': 3},
                {'id': 2, 'nombre': 'Contenedor Banio', 'nivel': 40, 'agente': 1}
            ],
            'baterias': [
                {'id': 1, 'nombre': 'Bateria 1', 'carga': 100, 'activa': True},
                {'id': 2, 'nombre': 'Bateria 2', 'carga': 80, 'activa': False}
            ]
        }

    def obtener(self, tipo):
        return self.dispositivos.get(tipo, [])

    def actualizar(self, tipo, id_dispositivo, datos):
        lista = self.dispositivos.get(tipo, [])
        for item in lista:
            if item['id'] == id_dispositivo:
                item.update(datos)
                return True
        return False
