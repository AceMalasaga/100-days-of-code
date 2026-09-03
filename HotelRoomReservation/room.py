class Room:

    def __init__(self, room_id, room_type, room_price):
        self.room_id = room_id
        self.room_type = room_type
        self.room_price = room_price
        self.is_room_vacant = True

    def room_info(self):
        status = "VACANT" if self.is_room_vacant else "OCCUPIED"
        print(f"[{self.room_id}] {self.room_type} - ₱{self.room_price}/night - [{status}]")

    def check_in(self):
        if self.is_room_vacant:
            self.is_room_vacant = False
            print(f"Guest checked into Room {self.room_id}!")
            return True
        else:
            print(f"Room {self.room_id} is already occupied!")
            return False

    def check_out(self, room_id):
        if not self.is_room_vacant:
            print(f"Guest checked out of Room {room_id}!")
            self.is_room_vacant = True
            return True
        else:
            print(f"Room {room_id} is already vacant!")
            return False


# room = Room("Room 101", "Standard", 1500)
# room.check_in()
# room.check_out("Room 101")
# room.room_info()