from vehicle import Vehicle
class Rental:

    def __init__(self):
        self.vehicle = {}

    def vehicle_rental_info(self):
        if not self.vehicle:
            print("No vehicles currently registered in the rental fleet.")
        else:
            for vehicle in self.vehicle.values():
                vehicle.vehicle_info()

    def add_vehicle(self, vehicle_id, vehicle_model, vehicle_rate, vehicle_mileage, is_rented=True):
        if vehicle_id in self.vehicle:
            print(f"{vehicle_id} already registered in the rental fleet.")
            return False
        else:
            self.vehicle[vehicle_id] = Vehicle(vehicle_id, vehicle_model, vehicle_rate, vehicle_mileage, is_rented)
            print(f"{vehicle_model} (ID: {vehicle_id}) added to the rental fleet at ₱{vehicle_rate}/day!.")
            return True

    def check_rented_vehicle(self, vehicle_id):
        if vehicle_id in self.vehicle:
            self.vehicle[vehicle_id].rent_vehicle()
        else:
            print(f"Vehicle ID '{vehicle_id}' not found in fleet.")

    def return_rented_vehicle(self, v_id, v_km):
        if v_id in self.vehicle:
            self.vehicle[v_id].return_vehicle(v_id, v_km)
        else:
            print(f"Vehicle ID '{v_id}' not found in fleet.")

# rental = Rental()
# rental.add_vehicle("V01", "Toyota Vios", 1500, 12500)
# rental.vehicle_rental_info()
# rental.check_rented_vehicle("V01")
# rental.return_rented_vehicle("V01", 1000)