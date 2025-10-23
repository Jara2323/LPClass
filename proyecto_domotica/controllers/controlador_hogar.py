from database.datos import BaseDatos
from models.luz import Luz
from models.termostato import Termostato
from models.contenedor_residuos import ContenedorResiduos
from models.bateria import Bateria

class ControladorHogar:

    def __init__(self):
        self._db = BaseDatos()

    def obtener_luces(self):
        datos = self._db.obtener('luces')
        return [Luz(**luz) for luz in datos]

    def obtener_luz(self, id_luz: int):
        for luz in self.obtener_luces():
            if luz.id == id_luz:
                return luz
        return None

    def encender_luz(self, id_luz: int) -> bool:
        luz = self.obtener_luz(id_luz)
        if luz:
            luz.encender()
            self._db.actualizar('luces', id_luz, {'encendida': True})
            return True
        return False

    def apagar_luz(self, id_luz: int) -> bool:
        luz = self.obtener_luz(id_luz)
        if luz:
            luz.apagar()
            self._db.actualizar('luces', id_luz, {'encendida': False})
            return True
        return False

    def alternar_luz(self, id_luz: int) -> bool:
        luz = self.obtener_luz(id_luz)
        if luz:
            luz.alternar()
            self._db.actualizar('luces', id_luz, {'encendida': luz.encendida})
            return True
        return False

    def obtener_termostatos(self):
        datos = self._db.obtener('termostatos')
        return [Termostato(**termo) for termo in datos]

    def obtener_termostato(self, id_termo: int):
        for termo in self.obtener_termostatos():
            if termo.id == id_termo:
                return termo
        return None

    def ajustar_temperatura(self, id_termo: int, nueva_temp: float) -> bool:
        termo = self.obtener_termostato(id_termo)
        if termo:
            termo.ajustar_objetivo(nueva_temp)
            self._db.actualizar('termostatos', id_termo, {'objetivo': nueva_temp})
            return True
        return False

    def simular_temperatura(self, id_termo: int, temp: float) -> bool:
        termo = self.obtener_termostato(id_termo)
        if termo:
            termo.temperatura = temp
            self._db.actualizar('termostatos', id_termo, {'temperatura': temp})
            return True
        return False

    def obtener_contenedores(self):
        datos = self._db.obtener('contenedores')
        return [ContenedorResiduos(**cont) for cont in datos]

    def obtener_contenedor(self, id_cont: int):
        for cont in self.obtener_contenedores():
            if cont.id == id_cont:
                return cont
        return None

    def vaciar_contenedor(self, id_cont: int) -> bool:
        cont = self.obtener_contenedor(id_cont)
        if cont:
            cont.vaciar()
            self._db.actualizar('contenedores', id_cont, {'nivel': 0})
            return True
        return False

    def actualizar_nivel(self, id_cont: int, nivel: int) -> bool:
        cont = self.obtener_contenedor(id_cont)
        if cont:
            cont.nivel = nivel
            self._db.actualizar('contenedores', id_cont, {'nivel': nivel})
            return True
        return False

    def contenedores_llenos(self):
        return [c for c in self.obtener_contenedores() if c.esta_lleno()]

    def obtener_baterias(self):
        datos = self._db.obtener('baterias')
        return [Bateria(**bat) for bat in datos]

    def obtener_bateria(self, id_bat: int):
        for bat in self.obtener_baterias():
            if bat.id == id_bat:
                return bat
        return None

    def verificar_bateria_completa(self) -> bool:
        return any(bat.esta_cargada() for bat in self.obtener_baterias())

    def cargar_bateria(self, id_bat: int, cantidad: int) -> bool:
        bat = self.obtener_bateria(id_bat)
        if bat:
            bat.cargar(cantidad)
            self._db.actualizar('baterias', id_bat, {'carga': bat.carga})
            return True
        return False

    def consumir_energia(self, cantidad: int) -> bool:
        for bat in self.obtener_baterias():
            if bat.activa:
                if bat.consumir(cantidad):
                    self._db.actualizar('baterias', bat.id, {'carga': bat.carga})
                    return True
        return False

    def obtener_todos_dispositivos(self):
        dispositivos = []
        dispositivos.extend(self.obtener_luces())
        dispositivos.extend(self.obtener_termostatos())
        dispositivos.extend(self.obtener_contenedores())
        return dispositivos

    def obtener_dispositivos_por_agente(self, agente: int):
        return [d for d in self.obtener_todos_dispositivos() if d.agente == agente]
