#Name: Unit Converter2.py
# Author: Estalin Peña
# Date Created: november 21, 2022
# Date Last Modified: november 21, 2022
# Purpose: Convert Weight (Pounds and Kilograms) and Distance (Metres and Feets))

#Fuction name: weight_measurement
#Description: Will Output the conversion of the temperature selected by the user
#Parameters: 
#            Val: Numeric value of the weight
#            Unit: The kind of we the user wants to convert
#Return value:The conversion of the temperature selected by the user


def weight_measurement(val, unit):
    pnd_to_kg = (val * 0.451)
    kg_to_pnd = (val /0.451)
    if unit.upper() =="KG":
        print ('{:.2f} {}'.format(pnd_to_kg, "Pounds"))
    if unit.upper() =="LB":
        print ('{:.2f} {}'.format(kg_to_pnd, "Kilograms"))

#Fuction name: distance_measurement
#Description: Will Output the conversion of the distance selected by the user
#Parameters: 
#            Val: Numeric value of the distance
#            Unit: The kind of distance the user wants to convert
#Return value:The conversion of the distance selected by the user

def distance_measurement(val, unit):
    meters_to_feet= (val * 3.281)
    feet_to_meters = (val /3.281)
    if unit.upper() == "M":
        print ('{:.2f} {}'.format(meters_to_feet, "Feet".strip()))
    if unit.upper() == "F":
        print ('{:.2f} {}'.format(feet_to_meters, "Metres".strip()))


while True:
    print(" ")#spaces between the information
    print("\t","\t", "\t",  "Welcome to the Unit Converter")#Displays the welcome message
    print(" ")#spaces between the information

    unit_selector = input("Please select the unit you wish to convert: 1) Weight 2) Distance: ")#Takes the type of unit the user wishes to convert
    while unit_selector != "1" and unit_selector != "2":
        print("Your input is incorrect")
        unit_selector = input("Please select the unit you wish to convert: 1) Weight 2) Distance: ")




    print(" - " *40)#separates the data printed with dashes

    if unit_selector == "1": #This evaluates the user selection  for weight
        while True:
            try:
                val = float(input("Please enter the measurement: "))#This takes the numeric value of the weight
            except:
                print("Please enter a valid value")
            else:
                break
        unit = input("'LB' Pounds or 'KG' Kilograms: ")#The user selects Pounds or Kilograms
        while unit.strip().upper() != "LB" and unit.strip().upper() != "KG":
            unit = input("'LB' Pounds or 'KG' Kilograms: ")
        weight_measurement(val, unit)#This returns the values from the function weight_measurement and  applies the formula
    elif unit_selector == "2":
        while True:  #This while evaluates either if the user wants to continue or not converting distance.
            try:
                val = float(input("Please enter the measurement: "))#This takes the numeric value of the weight
            except:
                print("Please enter a valid value")
            else:
                break
        unit = input("'M' Metres or 'FT' Feet: ")#The user selects Metes or Feets
        while unit.strip().upper() != "M" and unit.strip().upper() != "FT":
            unit = input("'M' Metres or 'FT' Feets: ")
        distance_measurement(val, unit)

    print(" - " *40)#separates the data printed with dashes

    goodBye = input("Do you wish to continue? [Yes/No]: ".strip())#This variable asks the user if wants to continue in the process
    print(" - " *40)#separates the data printed with dashes
    
    if goodBye.upper() == "Yes" or goodBye.upper() == "Y":
        continue
    elif goodBye.upper() == "No" or goodBye.upper() == "N":
        print("Have a great day!".strip())
        break
