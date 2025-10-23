from vehicle_repository import IVehicleRepository

# Se aplica el principio "O" de SOLID
class MongoDBRepository(IVehicleRepository):
    
    def get_all(this):
        return [
            {"brand": "Toyota", "model": "Corolla", "year": 2022, "vehicle_type": "Auto"},
            {"brand": "Volvo", "model": "FH16", "year": 2023, "vehicle_type": "Camión"},
            {"brand": "Yamaha", "model": "MT-07", "year": 2021, "vehicle_type": "Moto"}
        ]
