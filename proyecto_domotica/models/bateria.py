class Bateria:

    CAPACIDAD_MAXIMA = 100

    def __init__(self, id_bateria: int, nombre: str, carga: int, activa: bool):
        self._id = id_bateria
        self._nombre = nombre
        self._carga = carga
        self._activa = activa

    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def carga(self) -> int:
        return self._carga

    @carga.setter
    def carga(self, valor: int):
        if 0 <= valor <= self.CAPACIDAD_MAXIMA:
            self._carga = valor

    @property
    def activa(self) -> bool:
        return self._activa

    @activa.setter
    def activa(self, valor: bool):
        self._activa = valor

    def porcentaje_carga(self) -> float:
        return (self._carga / self.CAPACIDAD_MAXIMA) * 100

    def esta_cargada(self) -> bool:
        return self._carga == self.CAPACIDAD_MAXIMA

    def cargar(self, cantidad: int):
        self._carga = min(self._carga + cantidad, self.CAPACIDAD_MAXIMA)

    def consumir(self, cantidad: int) -> bool:
        if self._carga >= cantidad:
            self._carga -= cantidad
            return True
        return False

    def obtener_estado(self) -> str:
        porcentaje = self.porcentaje_carga()

        if porcentaje == 100:
            estado = "Carga completa"
        elif porcentaje >= 50:
            estado = "Carga buena"
        elif porcentaje >= 20:
            estado = "Carga baja"
        else:
            estado = "Carga critica"

        uso = "EN USO" if self._activa else "Standby"
        return f"{self._nombre} (ID:{self._id}) - {self._carga}% {estado} [{uso}]"

    def __str__(self):
        return self.obtener_estado()
