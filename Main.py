import read
import write
import operation

# Main program to handle user input
def main():
    print("\n\t\t\t Techno Property Nepal")
    print("\n\t\t\t Kamalpokhari, Kathmandu")
    print("\n\t\t\t Phone No: 9808433305")
    print("\n*")
    print("\n\t\t\t\t Have a good day")
    print("\n*")

    print("1. Show lands")
    print("2. Rent lands")
    print("3. Return land")
    print("4. exit")

    lines = read.land_read_details()

    while True:
        choice = input("\n\nEnter a number from the above options: ")
        if choice == "1":
            read.show_land_details(lines)
        elif choice == "2":
            lines = operation.rent_land(lines)
        elif choice == "3":
            lines = operation.return_land(lines)
        elif choice == "4":
            return
        
        else:
            print("Invalid input, please try again.")


main()
