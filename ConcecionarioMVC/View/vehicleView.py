class VehicleView:
    
    def showVehicles(this, vehiclesData):
        print("=== Lista de Vehículos Disponibles ===")
        for vehicle in vehiclesData:
            print(f"Marca: {vehicle.brand}, Modelo: {vehicle.model}, Año: {vehicle.year}, Tipo: {vehicle.vehicle_type}")
