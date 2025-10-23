from models.dispositivo_base import DispositivoBase

class ContenedorResiduos(DispositivoBase):

    CAPACIDAD_MAXIMA = 100
    UMBRAL_ALERTA = 80

    def __init__(self, id_contenedor: int, nombre: str, nivel: int, agente: int):
        super().__init__(id_contenedor, nombre, agente)
        self._nivel = nivel
        self._activo = True

    @property
    def nivel(self) -> int:
        return self._nivel

    @nivel.setter
    def nivel(self, valor: int):
        if 0 <= valor <= self.CAPACIDAD_MAXIMA:
            self._nivel = valor

    def encender(self):
        self._activo = True

    def apagar(self):
        self._activo = False

    def vaciar(self):
        self._nivel = 0

    def porcentaje(self) -> float:
        return (self._nivel / self.CAPACIDAD_MAXIMA) * 100

    def esta_lleno(self) -> bool:
        return self._nivel >= self.UMBRAL_ALERTA

    def obtener_estado(self) -> str:
        porcentaje = self.porcentaje()

        if porcentaje >= self.UMBRAL_ALERTA:
            estado = "LLENO - Vaciar urgente"
        elif porcentaje >= 50:
            estado = "Medio lleno"
        else:
            estado = "OK"

        return f"{self.obtener_info_basica()} - Nivel: {self._nivel}/{self.CAPACIDAD_MAXIMA} ({porcentaje:.0f}%) {estado}"

    def obtener_info(self) -> dict:
        info = super().obtener_info()
        info['nivel'] = self._nivel
        info['porcentaje'] = self.porcentaje()
        info['tipo'] = 'Contenedor'
        return info

    def __str__(self):
        return self.obtener_estado()
