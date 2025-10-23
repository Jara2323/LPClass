from Model.vehicle import Vehicle
from View.vehicleView import VehicleView
from Repositories.car_repository import IVehicleRepository

class VehicleController: 
    
    def __init__(this, repository: IVehicleRepository, view: VehicleView):
        this.repo = repository
        this.view = view

    # Implementación de una función de CRUD que sería llamada desde la vista
    def list_all_vehicles(this):
        vehiclesData = this.repo.get_all()
        this.view.showVehicles(vehiclesData)
