# 1. Deklarera ditt eget dictionary "car " med information om en bil 

car = {
    "Name" : "DeTomaso",
    "Model" : "Pantera GT5",
    "Year" : 1985
}

# 2. Skriv ut all data i din bil med print(car['nyckel']).

print(car["Name"])
print(car["Model"])
print(car["Year"])

# 3. Går det att göra flera dictionaries i en lista? Försök att “nästla” dictionaries i en lista så du kan ha flera bilar

car2 = {
    "Name" : "Volvo",
    "Model" : "S60",
    "Year" : 2025
}

cars = [car, car2]

# 4. Skriv ut samtliga bilar på ett snyggt sätt

for i in range(len(cars)):
    print(f"Name: {(cars[i])['Name']}")
    print(f"Model: {(cars[i])['Model']}")
    print(f"Year: {(cars[i])['Year']}")

# 5. Gör så man kan lägga till bil

Name = input("Write the name of the car you want to add: ")
Model = input("Write the model of the name you want to add: ")
Year = int(input("Write the year of the car you want to add: "))

car3 = {
    "Name" : Name,
    "Model" : Model,
    "Year" : Year
}
cars.append(car3)

# 6. Gör så man kan ta bort bil

removed_car = int(input("Write the number of the car you want to remove, (0-2): "))

cars.pop(removed_car)


# 7. Gör så man kan ändra bil

while True:
    try:
        car_edit = int(input("Choose a car you want to edit, (0-2)"))
        print(f"Name: {(cars[car_edit])['Name']}")
        print(f"Model: {(cars[car_edit])['Model']}")
        print(f"Year: {(cars[car_edit])['Year']}")

        
        edited_info = input("What info do you want to edit, (write key): ")

        if edited_info.lower() == "year":
            new_info = int(input("Write the new year: "))
            (cars[car_edit])["Year"] = new_info
            break
        elif edited_info.lower() == "model":
            new_info = input("Write the new model")
            (cars[car_edit])["Model"] = new_info
            break
        elif edited_info.lower() == "name":
            new_info = input("Write the new name: ")
            (cars[car_edit])["Name"] = new_info
            break
        else:
            print("You inputed something wrong")
            continue

    except:
        print("You inputed something wrong.")



# 8. ÖVERKURS: Kan du göra dictionaries i dictionaries (nästlade dictionaries)? Vad är fördelen/nackdelen jämfört med i en lista?



pupil1 = {
    "Name" : "Yester Smith",
    "Grade" : 4
}
pupil2 = {
    "Name" : "Shrek Harvey",
    "Grade" : 9
}


pupils_in_class = {
    "pupil1" : pupil1,
    "pupil2" : pupil2
}


# Fördelen är att de kan stora mer specifika värden för en specifik dictornary än en lista.

