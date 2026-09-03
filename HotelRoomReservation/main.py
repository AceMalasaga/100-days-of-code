from hotel import Hotel

is_hotel_operate = True
hotel = Hotel()

while is_hotel_operate:
    print("=== HOTEL RESERVATION SYSTEM ===")
    print("1. View All Rooms\n2. Add a New Room\n3. Check-In Guest\n4. Check-Out Guest\n5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        hotel.view_all_room()
    elif choice == 2:
        r_id = input("Enter room id: ").upper().strip()
        r_type = input("Enter room type: ")
        r_price = input("Enter room price: ")
        hotel.add_room(r_id, r_type, float(r_price))
    elif choice == 3:
        r_id = input("Enter room id: ").upper()
        hotel.check_in_room_by_id(r_id)
    elif choice == 4:
        r_id = input("Enter room id: ").upper()
        hotel.check_out_room_by_id(r_id)
    elif choice == 5:
        print("Exiting...")
        is_hotel_operate = False
    else:
        print(f"Invalid choice. Please try again.")

