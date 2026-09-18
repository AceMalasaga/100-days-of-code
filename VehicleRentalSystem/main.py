from rental import Rental

is_rental_open = True
rental = Rental()

while is_rental_open:
    print("=====Vehicle Rental System=====")
    print("1. View All Vehicle Info\n2. Add a New Vehicle\n3. Rent a vehicle\n4. Return a vehicle\n5. Exit")

    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        rental.vehicle_rental_info()
    elif user_choice == 2:
        v_id = input("Enter Vehicle ID: ")
        v_model = input("Enter Model: ")
        v_rate = int(input("Enter Daily Rate: "))
        v_mileage = float(input("Enter Initial Mileage (km): "))
        rental.add_vehicle(v_id, v_model, v_rate, v_mileage)
    elif user_choice == 3:
        v_id = input("Enter Vehicle ID to Rent: ")
        rental.check_rented_vehicle(v_id)
    elif user_choice == 4:
        v_id = input("Enter Vehicle ID to Return: ")
        v_mileage = float(input("Enter Distance Driven (km): "))
        rental.return_rented_vehicle(v_id, v_mileage)
    elif user_choice == 5:
        print("Exiting...")
        is_rental_open = False
    else:
        print("Invalid Input, please try again")
