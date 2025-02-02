from hotel_reservation import Hotel

def display_available_rooms(hotel):
    """Display available rooms in the hotel"""
    print("\nAvailable Rooms:")
    for room_type, num_rooms in hotel.rooms.items():
        print(f"{room_type}: {num_rooms} rooms available")

def main():
    # Example hotel setup
    hotel = Hotel("Grand Plaza", {"single": 10, "double": 5, "suite": 3})
    
    print(f"Welcome to {hotel.name}!\n")
    
    while True:
        print("\n--- Menu ---")
        print("1. View available rooms")
        print("2. Make a reservation")
        print("3. View reservations")
        print("4. Cancel a reservation")
        print("5. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == "1":
            display_available_rooms(hotel)
        
        elif choice == "2":
            guest_name = input("Enter your name: ")
            room_type = input("Enter room type (single, double, suite): ").lower()
            num_rooms = int(input(f"How many {room_type} rooms would you like to reserve? "))
            check_in = input("Enter check-in date (YYYY-MM-DD): ")
            check_out = input("Enter check-out date (YYYY-MM-DD): ")
            
            if hotel.make_reservation(guest_name, room_type, num_rooms, check_in, check_out):
                print(f"Reservation successful for {guest_name}.")
            else:
                print(f"Sorry, we do not have enough {room_type} rooms available.")
        
        elif choice == "3":
            reservations = hotel.view_reservations()
            print("\nCurrent Reservations:")
            if isinstance(reservations, list):
                for res in reservations:
                    print(f"Guest: {res['guest_name']}, Room: {res['room_type']}, {res['num_rooms']} rooms, "
                          f"Check-in: {res['check_in']}, Check-out: {res['check_out']}")
            else:
                print(reservations)

        elif choice == "4":
            guest_name = input("Enter your name to cancel the reservation: ")
            room_type = input("Enter room type (single, double, suite): ").lower()
            num_rooms = int(input(f"How many {room_type} rooms to cancel? "))
            check_in = input("Enter check-in date of the reservation (YYYY-MM-DD): ")
            check_out = input("Enter check-out date of the reservation (YYYY-MM-DD): ")
            
            if hotel.cancel_reservation(guest_name, room_type, num_rooms, check_in, check_out):
                print(f"Reservation canceled for {guest_name}.")
            else:
                print("Reservation not found.")
        
        elif choice == "5":
            print("Thank you for visiting! Goodbye!")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
