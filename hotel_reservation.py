class Hotel:
    def __init__(self, name, rooms):
        """Initialize hotel with name and available rooms"""
        self.name = name
        self.rooms = rooms  # a dictionary where key is room type and value is the number of rooms available
        self.reservations = []  # list to store all reservations

    def check_availability(self, room_type, num_rooms):
        """Check if the requested number of rooms are available"""
        if room_type in self.rooms:
            available_rooms = self.rooms[room_type]
            if available_rooms >= num_rooms:
                return True
            else:
                return False
        return False

    def make_reservation(self, guest_name, room_type, num_rooms, check_in, check_out):
        """Make a reservation if rooms are available"""
        if self.check_availability(room_type, num_rooms):
            reservation = {
                'guest_name': guest_name,
                'room_type': room_type,
                'num_rooms': num_rooms,
                'check_in': check_in,
                'check_out': check_out
            }
            # Store reservation and update available rooms
            self.reservations.append(reservation)
            self.rooms[room_type] -= num_rooms
            return True
        return False

    def view_reservations(self):
        """View all current reservations"""
        if not self.reservations:
            return "No reservations made yet."
        return self.reservations

    def cancel_reservation(self, guest_name, room_type, num_rooms, check_in, check_out):
        """Cancel a reservation and free the rooms"""
        for reservation in self.reservations:
            if (reservation['guest_name'] == guest_name and
                reservation['room_type'] == room_type and
                reservation['num_rooms'] == num_rooms and
                reservation['check_in'] == check_in and
                reservation['check_out'] == check_out):
                self.reservations.remove(reservation)
                self.rooms[room_type] += num_rooms
                return True
        return False
