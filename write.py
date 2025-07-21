import datetime

# Function to generate rent invoice      
def generate_rent_invoice(rented_lands, customer_name, duration):
    total_amount = rented_lands['price'] * duration
    rent_note = "Rent Invoice\n\n"
    rent_note += "Kitta Number: " + rented_lands['kitta_number'] + "\n"
    rent_note += "City: " + rented_lands['city'] + "\n"
    rent_note += "Direction: " + rented_lands['direction'] + "\n"
    rent_note += "Area: " + rented_lands['area'] + " anna\n"
    rent_note += "Customer Name: " + customer_name + "\n"
    rent_note += "Date and Time of Rent: " + str(datetime.datetime.now()) + "\n\n"
    rent_note += "Duration: " + str(duration) + " months\n"
    rent_note += "Total Amount: NPR " + str(total_amount) + "\n"
    
    # Get the current time
    now = datetime.datetime.now()
    file_name = "rentInvoice_" + str(now.year) + str(now.month) + str(now.day) + "_" + str(now.hour) + str(now.minute) + str(now.second) + ".txt"
    
    with open(file_name, 'w') as file:
        file.write(rent_note)

    print("Rent invoice generated successfully. Check", file_name)

# Function to generate return invoice
def generate_return_invoice(customer_name, phone, address,time1, time2, returned_lands, fine, total_price ):
    return_note = "Rent Invoice\n\n"
    return_note += "Kitta Number: " + returned_lands['kitta_number'] + "\n"
    return_note += "City: " + returned_lands['city'] + "\n"
    return_note += "Direction: " + returned_lands['direction'] + "\n"
    return_note += "Area: " + returned_lands['area'] + " anna\n"
    return_note += "Customer Name: " + customer_name + "\n"
    return_note += "Date and Time of Rent: " + str(datetime.datetime.now()) + "\n\n"
    return_note += "Duration while rented: " + str(time1) + " months\n"
    return_note += "Duration while returned: " + str(time2) + " months\n"
    return_note += "Total Amount: NPR " + str(total_price) + "\n"

    # Get the current time
    now = datetime.datetime.now()
    file_name = "returnInvoice_" + str(now.year) + str(now.month) + str(now.day) + "_" + str(now.hour) + str(now.minute) + str(now.second) + ".txt"
    
    with open(file_name, 'w') as file:
        file.write(return_note)

    print("Return invoice generated successfully. Check", file_name)
