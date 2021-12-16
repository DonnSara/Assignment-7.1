class Vehicle:
    """A simple attempt to model a vehicle."""

    def __init__(self, make, model, color, fuelType, options):
        """Initialize vehicle attributes."""
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options

    def getMake():
        """Get the vehicle's make."""
        vehicle_make = input("What is the vehicle's make? ")
        return vehicle_make.title()

    def getModel():
        """Get the vehicle's model."""
        vehicle_model = input("What is the vehicle's model? ")
        return vehicle_model.title()

    def getColor():
        """Get the vehicle's color."""
        vehicle_color = input("What is the vehicle's color? ")
        return vehicle_color

    def getFuelType():
        """Get the vehicle's fuel type."""
        vehicle_fuel_type = input("What is the vehicle's fuel type? ")
        return vehicle_fuel_type

    def getOptions():
        """Get the vehicle's options."""
        vehicle_options = ['power mirrors', 'power locks', 'remote start', 'backup camera', 'bluetooth', 'cruise control', 'airbags', 'air conditioning']
        num = 1
        for option in vehicle_options:#print options
            print(str(num) + " - " + option)
            num += 1
        user_options = input("Which of the above attributes do you want to add to your vehicle? \nat least one is needed.\nJust write the numbers matching the attributes, seperated by a space.\n")
        user_options = user_options.split()#save users options in list
        index = 0
        for option in user_options:#replace number with actual attribute
            if option == '1':
                user_options[index] = 'power mirrors'
            elif option == "2":
                user_options[index] = 'power locks'
            elif option == "3":
                user_options[index] = 'remote start'
            elif option == "4":
                user_options[index] = 'backup camera'
            elif option == "5":
                user_options[index] = 'bluetooth'
            elif option == "6":
                user_options[index] = 'cruise control'
            elif option == "7":
                user_options[index] = 'airbags'
            elif option == "8":
                user_options[index] = 'air conditioning'
            else:
                print("No such option!")
                Vehicle.getOptions()
            index += 1
        return user_options


class Car(Vehicle):
    """A simple attempt to model a vehicle, specifically a car."""

    def __init__(self, engineSize, numDoors):
        """Initialize car attributes."""
        self.engineSize = engineSize
        self.numDoors = numDoors

    def getEngineSize():
        """Get the car's engine size."""
        car_engine_size = input("What is the car's engine size? ")
        return car_engine_size

    def getNumDoors():
        """Get the car's number of doors."""
        car_num_doors = input("How many doors does the car have? ")
        return car_num_doors


class Pickup(Vehicle):
    """A simple attempt to model a vehicle, specifically a pickup."""

    def __init__(self, cabStyle, bedLength):
        """Initialize pickup attributes."""
        self.cabStyle = cabStyle
        self.bedLength = bedLength

    def getCabStyle():
        """Get the pickup's cab style."""
        pickup_cab_style = input("What is the pickup's cab style? ")
        return pickup_cab_style

    def getBedLength():
        """Get the pickup's bed length."""
        pickup_bed_length = input("What's the pickup's bed length? ")
        return pickup_bed_length


def addVehicle():
    """Allow user to add vehicle to garage."""
    cars = 0
    pickups = 0
    vehicleList = []
    options = []
    answer = True
    while answer == True:
        print("A minimum of one car and one pickup truck must be added.")
        vehicle = input("What kind of vehicle do you want to add, a car or a pickup?\nWrite 1 for car and 2 for pickup:\n")
        if vehicle != "1" and vehicle != "2":
            print("No such option!")
            addVehicle()
        Vehicle("default", "default", "default", "default", "default") 
        make = Vehicle.getMake()
        model = Vehicle.getModel()
        color = Vehicle.getColor()
        fuelType = Vehicle.getFuelType()
        optionsTemp = Vehicle.getOptions()
        options = []
        options.extend(optionsTemp)
        if vehicle == "1":
            Car("default", "default")
            engineSize = Car.getEngineSize()
            numDoors = Car.getNumDoors()
            vehicleList.extend(['Vehicle type: ', 'car', 'Make: ', make, 'Model: ', model, 'Color: ', color, 'Fuel type: ', fuelType, 'Engine size: ', engineSize, 'Number of doors: ', numDoors, 'Other features: ', options])
            cars += 1
        else: #vehicle == "2"
            Pickup("default", "default")
            cabStyle = Pickup.getCabStyle()
            bedLength = Pickup.getBedLength()
            vehicleList.extend(['Vehicle type: ', 'pickup', 'Make: ', make, 'Model: ', model, 'Color: ', color, 'Fuel type: ', fuelType, 'Cab style: ', cabStyle, 'Bed length: ', bedLength, 'Other features: ', options])
            pickups += 1
        
        numAnswer = input("Do you want to add another vehicle to your virtual garage?\nWrite 1 for 'Yes' and 2 for 'No':\n")
        numAnswer = int(numAnswer)
        if numAnswer == 1:
            answer = True
        elif numAnswer == 2:
            if cars == 0 or pickups == 0:
                answer = True
            else:
                answer = False
        else:
            print("No such option!")
            answer = True
    return vehicleList    


print("Hi, I will be creating a virtual garage for you where you can add cars and pickup trucks, together with their attributes.")
vehicleList = []
vehicleList.extend(addVehicle())
    
print("The folowing vehicles with the characteristics listed below are in your virtual garage:")
tempNum = 1
for item in vehicleList: #print each vehicle    
    if tempNum % 2 != 0: #it's odd, title for description
        print(item, end="")
    elif tempNum % 2 == 0: #it's even, description
        if isinstance(item, list):#options
            x = ", ".join(item)
            print(x)
            print("\n")#to space vehicles.
        else:
            print(item)
    tempNum += 1 