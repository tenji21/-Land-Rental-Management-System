# operation.py

import read
import write
#Function to generate rent land
def rent_land(lines):
    rent_id = input("Enter the ID of the land you want to rent: ")

    # Update the availability status
    updated_lines = []
    rented_land_details = ""
    land_found = False

    for line in lines:
        parts = line.split(',')
        if parts[0] == rent_id:
            land_found = True
            if parts[-1].strip() == 'Available':
                parts[-1] = 'Not Available\n'
                rented_land_details = ','.join(parts)
                updated_lines.append(rented_land_details)
                rented_lands = {
                    'kitta_number': parts[0],
                    'city': parts[1],
                    'direction': parts[2],
                    'area': parts[3],
                    'price': float(parts[4])
                }
            else:
                print("The selected land is already rented.")
                return lines
        else:
            updated_lines.append(line.strip() + '\n')

    if not land_found:
        print("The land ID entered does not exist.")
        return lines

    #updated lines 
    with open('land_details.txt', 'w') as file:
        for line in updated_lines:
            file.write(line)

    # Get user details
    customer_name = input("Enter your name: ")
    address = input("Enter your address: ")
    try1= True
    while(try1==True):
        try:
            duration = int(input("Enter the rental duration in months: "))
            try1=False
        except:
            print("Enter the valid duration")
        

    
    write.generate_rent_invoice(rented_lands, customer_name, duration)
    return updated_lines


# Generate the return invoice
def return_land(lines):
    return_id = input("Enter the ID of the land you want to return: ")

    # Update the availability status
    update_lines = []
    renturning_land_details = ""
    land_found = False

    for line in lines:
        parts = line.split(',')
        if parts[0] == return_id:
            land_found = True
            if parts[-1].strip() == 'Not Available':
                parts[-1] = '   Available\n'
                renturning_land_details = ','.join(parts)
                update_lines.append(renturning_land_details)
                returned_lands = {
                    'kitta_number': parts[0],
                    'city': parts[1],
                    'direction': parts[2],
                    'area': parts[3],
                    'price': float(parts[4])  
                }
            else:
                print("The selected land is not rented.")
                return lines
        else:
            update_lines.append(line.strip() + '\n')

    if not land_found:
        print("The land ID entered does not exist.")
        return lines
    
    with open('land_details.txt', 'w') as file:
        for line in update_lines:
            file.write(line)
        
        #Fine if land is returned late
    customer_name = input("Enter your name: ")
    try2= True
    while(try2==True):
        try:
            phone = input("Enter your phone number: ")
            try2=False
        except:
            print("Enter the valid phone number")
    address = input("Enter your address: ")
    try3= True
    while(try3==True):
        try:
            time1 = int(input("land was rented for: "))
            try3=False
        except:
            print("Enter the valid rented land ")
    try4= True
    while(try4==True):
        try:
            time2 = int(input("land was returned after: "))
            try4=False
        except:
            print("Enter the valid returned land")
    
    if time2 > time1:
        total_time = time2 - time1
        fine = int(parts[-2]) * total_time * 0.1
        
    else:
        fine = 0
    total_price = returned_lands['price'] * time2 + fine


        
    print("Land returned successfully")
    write.generate_return_invoice(customer_name, phone, address, time1, time2, returned_lands, fine, total_price )
    return update_lines

