# CarFinder Program for AutoCountry

# List of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")

def print_vehicles():
    print("\nAuthorized Vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")
    print()  # Print a newline for spacing after the list

def search_vehicle():
    search_query = input("\nPlease Enter the full Vehicle name: ")
    if search_query in AllowedVehiclesList:
        print(f"\n'{search_query}' is an authorized vehicle.")
    else:
        print(f"\n'{search_query}'is not an authorized vehicle, if you received this in error please check the spelling and try again")
    print()  # Print a newline for spacing after search results

def main():
    while True:
        display_menu()
        user_input = input("\nEnter your choice: ")

        if user_input == '1':
            print_vehicles()
        elif user_input == '2':
            search_vehicle()
        elif user_input == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

# Program entry point
if __name__ == "__main__":
    main()