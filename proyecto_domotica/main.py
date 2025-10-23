from controllers.controlador_hogar import ControladorHogar
from views.vista_consola import VistaConsola

class App:

    def __init__(self):
        self.controlador = ControladorHogar()
        self.vista = VistaConsola()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu_principal()
            opcion = self.vista.solicitar_entrada("Seleccione una opcion")

            if opcion == "1":
                self._menu_luces()
            elif opcion == "2":
                self._menu_termostatos()
            elif opcion == "3":
                self._menu_contenedores()
            elif opcion == "4":
                self._menu_baterias()
            elif opcion == "5":
                self._demostrar_sistema()
            elif opcion == "6":
                self._menu_por_agente()
            elif opcion == "0":
                self.vista.mostrar_mensaje("Hasta luego", "info")
                break
            else:
                self.vista.mostrar_mensaje("Opcion invalida", "error")

    def _menu_luces(self):
        while True:
            self.vista.mostrar_menu_luces()
            opcion = self.vista.solicitar_entrada("Opcion")

            if opcion == "1":
                luces = self.controlador.obtener_luces()
                self.vista.mostrar_lista("LUCES DEL SISTEMA", luces)

            elif opcion == "2":
                luces = self.controlador.obtener_luces()
                self.vista.mostrar_lista("Luces disponibles", luces)
                id_luz = int(self.vista.solicitar_entrada("ID de la luz"))
                if self.controlador.encender_luz(id_luz):
                    self.vista.mostrar_mensaje("Luz encendida", "exito")
                    self.controlador.consumir_energia(5)
                else:
                    self.vista.mostrar_mensaje("No se pudo encender", "error")

            elif opcion == "3":
                luces = self.controlador.obtener_luces()
                self.vista.mostrar_lista("Luces disponibles", luces)
                id_luz = int(self.vista.solicitar_entrada("ID de la luz"))
                if self.controlador.apagar_luz(id_luz):
                    self.vista.mostrar_mensaje("Luz apagada", "exito")
                else:
                    self.vista.mostrar_mensaje("No se pudo apagar", "error")

            elif opcion == "4":
                luces = self.controlador.obtener_luces()
                self.vista.mostrar_lista("Luces disponibles", luces)
                id_luz = int(self.vista.solicitar_entrada("ID de la luz"))
                if self.controlador.alternar_luz(id_luz):
                    self.vista.mostrar_mensaje("Estado alternado", "exito")
                    self.controlador.consumir_energia(5)
                else:
                    self.vista.mostrar_mensaje("No se pudo alternar", "error")

            elif opcion == "0":
                break

    def _menu_termostatos(self):
        while True:
            self.vista.mostrar_menu_termostatos()
            opcion = self.vista.solicitar_entrada("Opcion")

            if opcion == "1":
                termos = self.controlador.obtener_termostatos()
                self.vista.mostrar_lista("TERMOSTATOS DEL SISTEMA", termos)

            elif opcion == "2":
                termos = self.controlador.obtener_termostatos()
                self.vista.mostrar_lista("Termostatos disponibles", termos)
                id_termo = int(self.vista.solicitar_entrada("ID del termostato"))
                temp = float(self.vista.solicitar_entrada("Nueva temperatura objetivo"))
                if self.controlador.ajustar_temperatura(id_termo, temp):
                    self.vista.mostrar_mensaje(f"Temperatura ajustada a {temp}C", "exito")
                    self.controlador.consumir_energia(10)
                else:
                    self.vista.mostrar_mensaje("No se pudo ajustar", "error")

            elif opcion == "3":
                termos = self.controlador.obtener_termostatos()
                self.vista.mostrar_lista("Termostatos disponibles", termos)
                id_termo = int(self.vista.solicitar_entrada("ID del termostato"))
                temp = float(self.vista.solicitar_entrada("Temperatura actual simulada"))
                if self.controlador.simular_temperatura(id_termo, temp):
                    self.vista.mostrar_mensaje(f"Temperatura actualizada a {temp}C", "exito")
                else:
                    self.vista.mostrar_mensaje("No se pudo actualizar", "error")

            elif opcion == "0":
                break

    def _menu_contenedores(self):
        while True:
            self.vista.mostrar_menu_contenedores()
            opcion = self.vista.solicitar_entrada("Opcion")

            if opcion == "1":
                contenedores = self.controlador.obtener_contenedores()
                self.vista.mostrar_lista("CONTENEDORES DEL SISTEMA", contenedores)

            elif opcion == "2":
                contenedores = self.controlador.obtener_contenedores()
                self.vista.mostrar_lista("Contenedores disponibles", contenedores)
                id_cont = int(self.vista.solicitar_entrada("ID del contenedor"))
                if self.controlador.vaciar_contenedor(id_cont):
                    self.vista.mostrar_mensaje("Contenedor vaciado", "exito")
                    self.controlador.consumir_energia(8)
                else:
                    self.vista.mostrar_mensaje("No se pudo vaciar", "error")

            elif opcion == "3":
                contenedores = self.controlador.obtener_contenedores()
                self.vista.mostrar_lista("Contenedores disponibles", contenedores)
                id_cont = int(self.vista.solicitar_entrada("ID del contenedor"))
                nivel = int(self.vista.solicitar_entrada("Nuevo nivel (0-100)"))
                if self.controlador.actualizar_nivel(id_cont, nivel):
                    self.vista.mostrar_mensaje(f"Nivel actualizado a {nivel}", "exito")
                else:
                    self.vista.mostrar_mensaje("No se pudo actualizar", "error")

            elif opcion == "4":
                llenos = self.controlador.contenedores_llenos()
                if llenos:
                    self.vista.mostrar_lista("CONTENEDORES LLENOS (>80%)", llenos)
                    self.vista.mostrar_mensaje("Hay contenedores que necesitan vaciarse", "alerta")
                else:
                    self.vista.mostrar_mensaje("Todos los contenedores estan OK", "exito")

            elif opcion == "0":
                break

    def _menu_baterias(self):
        while True:
            self.vista.mostrar_menu_baterias()
            opcion = self.vista.solicitar_entrada("Opcion")

            if opcion == "1":
                baterias = self.controlador.obtener_baterias()
                self.vista.mostrar_lista("BATERIAS DEL SISTEMA", baterias)

                if self.controlador.verificar_bateria_completa():
                    self.vista.mostrar_mensaje("Al menos una bateria esta al 100%", "exito")
                else:
                    self.vista.mostrar_mensaje("Ninguna bateria esta al 100%", "alerta")

            elif opcion == "2":
                baterias = self.controlador.obtener_baterias()
                self.vista.mostrar_lista("Baterias disponibles", baterias)
                id_bat = int(self.vista.solicitar_entrada("ID de la bateria"))
                cantidad = int(self.vista.solicitar_entrada("Cantidad a cargar (0-100)"))
                if self.controlador.cargar_bateria(id_bat, cantidad):
                    self.vista.mostrar_mensaje(f"Bateria cargada con {cantidad} unidades", "exito")
                else:
                    self.vista.mostrar_mensaje("No se pudo cargar", "error")

            elif opcion == "3":
                cantidad = int(self.vista.solicitar_entrada("Cantidad de energia a consumir"))
                if self.controlador.consumir_energia(cantidad):
                    self.vista.mostrar_mensaje(f"Consumidos {cantidad} unidades de energia", "exito")
                else:
                    self.vista.mostrar_mensaje("No hay suficiente energia", "error")

            elif opcion == "0":
                break

    def _demostrar_sistema(self):
        print("\n" + "="*70)
        print(" ESTADO DEL SISTEMA ".center(70))
        print("="*70)

        dispositivos = self.controlador.obtener_todos_dispositivos()
        baterias = self.controlador.obtener_baterias()

        self.vista.mostrar_lista("TODOS LOS DISPOSITIVOS", dispositivos)
        self.vista.mostrar_lista("BATERIAS", baterias)

    def _menu_por_agente(self):
        print("\n--- DISPOSITIVOS POR AGENTE ---")
        print("Agente 1, Agente 2, Agente 3")
        agente = int(self.vista.solicitar_entrada("Numero de agente (1-3)"))

        dispositivos = self.controlador.obtener_dispositivos_por_agente(agente)
        self.vista.mostrar_lista(f"DISPOSITIVOS DEL AGENTE {agente}", dispositivos)


def main():
    print("\n" + "="*70)
    print(" SISTEMA DE AUTOMATIZACION DEL HOGAR ".center(70))
    print("="*70)

    app = App()
    app.ejecutar()


if __name__ == "__main__":
    main()
