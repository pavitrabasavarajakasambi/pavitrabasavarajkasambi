
    def park_vehicle(self):
        if self.available_slots > 0:
            vehicle_number = input("Enter vehicle number: ")
            self.parked_vehicles[vehicle_number] = True
            self.available_slots -= 1
            print("Vehicle parked successfully!")
        else:
            print("Parking space is full.")

    def exit_parking(self):
        vehicle_number = input("Enter vehicle number: ")
        if vehicle_number in self.parked_vehicles:
            del self.parked_vehicles[vehicle_number]
            self.available_slots += 1
            print("Vehicle exited successfully!")
        else:
            print("Vehicle not found in parking space.")

    def display_status(self):
        print("Available slots:", self.available_slots)
        print("Parked vehicles:", list(self.parked_vehicles.keys()))


parking = ParkingSpace(20)

while True:
    print("\n1. Park Vehicle\n2. Exit Parking\n3. Display Status\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        parking.park_vehicle()
    elif choice == '2':
        parking.exit_parking()
    elif choice == '3':
        parking.display_status()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose again.")
