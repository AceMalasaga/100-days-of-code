from room import Room

class Hotel:

    def __init__(self):
        self.hotel_room = {}

    def view_all_room(self):
        if not self.hotel_room:
            print("No rooms currently registered in the hotel.")
        else:
            print("=== ALL ROOMS ===")
            for room in self.hotel_room.values():
                room.room_info()

    def add_room(self, room_id, room_type, room_price):
        """Add a new room record"""
        if room_id in self.hotel_room:
            print(f"Room {room_id} already exists in the hotel!")
            return False
        else:
            self.hotel_room[room_id] = Room(room_id, room_type, room_price)
            return True

    def check_in_room_by_id(self, room_id):
        if room_id in self.hotel_room:
            self.hotel_room[room_id].check_in()
            return True
        else:
            print(f"Room {room_id} does not exist in the hotel!")
            return False

    def check_out_room_by_id(self, room_id):
        if room_id in self.hotel_room:
            self.hotel_room[room_id].check_out(room_id)
            return True
        else:
            print(f"Room {room_id} does not exist in the hotel!")
            return False
#
# hotel = Hotel()
# hotel.add_room("101","Standard",1500)
# hotel.check_in_room_by_id("101")
# hotel.check_out_room_by_id("101")
# hotel.view_all_room()