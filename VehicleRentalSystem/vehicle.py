class Vehicle:
    def __init__(self, vehicle_id, vehicle_model, vehicle_rate, vehicle_mileage, is_rented):
        self.vehicle_id = vehicle_id
        self.vehicle_model = vehicle_model
        self.vehicle_rate = vehicle_rate
        self.vehicle_mileage = vehicle_mileage
        self.is_rented = is_rented

    def vehicle_info(self):
        if self.is_rented:
            status = "Available"
        else:
            status = "Rented"
        print(f"[{self.vehicle_id}] {self.vehicle_model} - ₱{float(self.vehicle_rate)}/day - "
              f"Mileage: {self.vehicle_mileage} km - {status}")

    def rent_vehicle(self):
        if self.is_rented:
            self.is_rented = False
            print(f"You have rented {self.vehicle_model} for ₱{float(self.vehicle_rate)}/day!")
            return True
        else:
            print(f"{self.vehicle_model} is currently rented out!")
            return False

    def return_vehicle(self, vehicle_id, distance_driven):
        if not self.is_rented:
            self.is_rented = True
            self.vehicle_mileage += distance_driven
            if self.is_rented:
                status = "Available"
            else:
                status = "Rented"
            print(f"Returned {self.vehicle_model}! Updated mileage: {float(self.vehicle_mileage)} km - {status}")
            return True
        else:
            print(f"The {vehicle_id}/{self.vehicle_model} was not rented out!")
            return False


# vehicle = Vehicle("V01", "Toyota Vios", 1500, 12500, True)
# vehicle.vehicle_info()
# vehicle.rent_vehicle()
# vehicle.return_vehicle("V01", 2500)