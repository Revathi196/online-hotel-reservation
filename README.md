# Hotel Reservation System

This is a simple command-line hotel reservation system that allows users to make reservations, view current reservations, cancel reservations, and check room availability. The system is built with Python and is designed to simulate an online hotel reservation process.

## Features

- **View available rooms**: Check how many rooms are available for different room types (e.g., single, double, suite).
- **Make a reservation**: Reserve rooms for a guest with specific check-in and check-out dates.
- **View reservations**: List all current reservations with details.
- **Cancel a reservation**: Cancel a previously made reservation and free up the rooms.

## Files in the Repository

### 1. `hotel_reservation.py`

This file contains the core functionality of the hotel reservation system, including:

- **`Hotel` class**: Manages the available rooms, reservations, and booking processes.
  - **`check_availability(room_type, num_rooms)`**: Checks if the required number of rooms are available for a specific room type.
  - **`make_reservation(guest_name, room_type, num_rooms, check_in, check_out)`**: Books the rooms if they are available.
  - **`view_reservations()`**: Lists all reservations made.
  - **`cancel_reservation(guest_name, room_type, num_rooms, check_in, check_out)`**: Cancels an existing reservation and frees up the rooms.

### 2. `main.py`

This is the entry point for the system. It provides an interactive menu where the user can choose to:
- View available rooms.
- Make a reservation.
- View current reservations.
- Cancel a reservation.
- Exit the system.

The file imports the `Hotel` class from `hotel_reservation.py` and allows interaction with the system through the terminal.

## How to Run

1. **Install Python**: Ensure that you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Download the repository**: Clone or download the repository files onto your local machine.

3. **Run the code**:
   Open your terminal or command prompt, navigate to the folder where the files are saved, and run the following command:
   
   ```bash
   python main.py
