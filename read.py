# Function to read land details from text file
def land_read_details():
     file = open('land_details.txt', 'r')
     lines = file.readlines()
     file.close()
     return lines
    

# Function to display land details in a table format
def show_land_details(lines):
    file = open('Land_details.txt', 'r') 
    lines = file.readlines()
    file.close()
    
    # Print the table header
    header = lines[0].split(',')
    for column in header:
        if column[-1] == '\n':
            column = column[:-1]
        print(column, end='\t')
    print()

    # Print the table rows
    for line in lines[1:]:
        row = line.split(',')
        for cell in row:
            if cell[-1] == '\n':
                cell = cell[:-1]
            print(cell, end='\t')
        print()
