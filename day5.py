# Multi-Room Type Booking System

single_rooms = 20
double_rooms = 35
single_cost = 4000
double_cost = 7000

print("Welcome to the Room Booking System")

#user details

name = input("Enter your name: ")
single_needed = int(input("Enter number of single rooms to book: "))
double_needed = int(input("Enter number of double rooms to book: "))

# Check validity
if single_needed < 0 or double_needed < 0:
    print("Invalid input. Enter positive numbers for rooms.")
else:
    # Check availability
    if single_needed <= single_rooms and double_needed <= double_rooms:
        single_rooms -= single_needed
        double_rooms -= double_needed
        total_cost = single_needed * single_cost + double_needed * double_cost
        print(f"\nBooking confirmed for {name}.")
        print(f"Single rooms booked: {single_needed}, Double rooms booked: {double_needed}")
        print(f"Single rooms remaining: {single_rooms}, Double rooms remaining: {double_rooms}")
        print(f"Total cost: ₹{total_cost}")
    else:
        # it handles  insufficient rooms
        if single_needed > single_rooms and double_needed > double_rooms:
            print(f"Sorry {name}, not enough single or double rooms available.")
        elif single_needed > single_rooms:
            print(f"Sorry {name}, only {single_rooms} single rooms are available.")
        else:
            print(f"Sorry {name}, only {double_rooms} double rooms are available.")
