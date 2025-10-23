class Report:
    def __init__(self, data):
        self.data = data

    def calcular_estads(self):
        pass

# Interfaz de estrategia
class SaveStrategy:
    def guardar(self, data):
        raise NotImplementedError

class ExcelSaveStrategy(SaveStrategy):
    def guardar(self, data):
        print("Generando reporte en EXCEL")

class PDFSaveStrategy(SaveStrategy):
    def guardar(self, data):
        print("Generando reporte en PDF")

class CSVSaveStrategy(SaveStrategy):
    def guardar(self, data):
        print("Generando reporte en CSV")

class ReportSaver:
    def __init__(self, strategy: SaveStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SaveStrategy):
        self.strategy = strategy

    def guardar_archivo(self, data):
        self.strategy.guardar(data)

class ReportNotifier:
    def notificar_cambios(self, data):
        print(f"Hubo un cambio en los datos: {data}")

# Ejemplo de uso:
if __name__ == "__main__":
    datos = [1, 2, 3]
    reporte = Report(datos)
    notifier = ReportNotifier()

    # Guardar como PDF
    saver = ReportSaver(PDFSaveStrategy())
    saver.guardar_archivo(reporte.data)

    # Cambiar a EXCEL
    saver.set_strategy(ExcelSaveStrategy())
    saver.guardar_archivo(reporte.data)

    # Cambiar a CSV
    saver.set_strategy(CSVSaveStrategy())
    saver.guardar_archivo(reporte.data)

    notifier.notificar_cambios(reporte.data)