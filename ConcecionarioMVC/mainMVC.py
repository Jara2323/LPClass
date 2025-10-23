from Controller.VehicleController import VehicleController
from View.VehicleView import VehicleView
from Repositories.mongodb_repository import MongoDBRepository

if __name__ == "__main__":
    repo = MongoDBRepository()
    view = VehicleView()
    controller = VehicleController(repo, view)
    controller.list_all_vehicles()
