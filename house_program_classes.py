# room class takes in user defined room data and stores it on itself
class Room:

    def __init__(self, room_data):
       
        self.room_name = room_data['room_name']
        self.square_feet = room_data['square_feet']
        self.number_windows = room_data['number_windows']
        self.has_fan = room_data['has_fan']
        self.number_outlets = room_data['number_outlets']
        self.floor_material = room_data['floor_material']
        self.number_lights = room_data['number_lights']
        
    # this method formats how the object or instance will appear when printed to the console only
    def __repr__(self):
        return (f"\n {self.room_name} ... square feet: {self.square_feet}, windows: {self.number_windows}, has fan? {self.has_fan}, outlets: {self.number_outlets}, floor: {self.floor_material}, lights: {self.number_lights} \n")

# house class takes room data and creates those rooms using the room class
# then stores the houses's room objects on itself in an array. Also takes in other house data
class House():

    def __init__(self):

        #assigns the values to self from the house_data dictionary passed in for the particular house 
        self.address = None
        self.price = None
        self.rooms = []
        self.color = None
        self.roof_material = None
        self.has_garage = None
        self.square_feet = None
        self.rooms_data = None
      
    # this class iterates through the room data supplied to the house class
    # and spawns instances of rooms using the room class
    # then stores the rooms on the house class via self
    def create_rooms(self):

        # the_room_name becomes each key of the self.rooms_data dictionary as it iterates
        for the_room_name in self.rooms_data:

            # the_room_data becomes the value stored under the "the_room_name" key
            # in the self.rooms_data dictionary
            the_room_data = self.rooms_data[the_room_name]

            # this becomes an instance of the Room class, and passes in the data for that particular room
            the_room_object = self.Room_class(the_room_data)

            # appends the spawned room object to the self of the house instance
            self.rooms.append(the_room_object)

    # iterates through all generated room objects and adds their square feet to total
    # the house's square feet
    def calculate_house_size(self):

        total_square_feet = 0
        i = 0

        # iterates through the house's rooms and adds their square feet to a total
        while i < len(self.rooms):

            the_room_obj = self.rooms[i]
            room_square_feet = the_room_obj.square_feet

            total_square_feet = total_square_feet + room_square_feet

            i += 1

        # assigns the new total square feet to the house object's self
        self.square_feet = total_square_feet

    # formats how the house object will appear when printed to the console only
    def __repr__(self):

        return (f"\n address: {self.address} \n price: {self.price} \n square feet: {self.square_feet} \n color: {self.color} \n roof: {self.roof_material} \n has garage? {self.has_garage} \n rooms: {self.rooms} \n")

class House_Builder():

    def __init__(self):

        self.house = House()
        self.creat_house()      
        
    def creat_house(self):

        house_attributes = ['address',
        'price',
        'rooms',
        'color',
        'roof_material',
        'has_garage']

        for house_attribute in house_attributes:

            user_input = input(f"enter {house_attribute}: ")
            setattr(self.house, house_attribute, user_input)


        print(self.house)


# this class serves as the main logic container of the app
class Neighboorhood_Program:

    # this init method runs once, it's just a function that gets ran when the new instance 
    # is spawned. It takes in the house data in the addresses argument
    def __init__(self, addresses):
        
        # # applies the addresses ( house_data ) to the instance of the class
        # self.addresses = addresses

        # # loops through each address or house in the self.addresses dictionary
        # for address in self.addresses:

        #     # this variable becomes the house data value for each particular house key in the addresses dictionary
        #     # so house_data is its own dictionary that contains all of the data for a house
        #     house_data = self.addresses[address]

        #     # runs the add_a_new_house method and passes in the house data dictionary
        #     self.add_a_new_house(house_data)
        house_builder = House_Builder()

    # creats a house
    def add_a_new_house(self, house_data):

        # creates an instance of the house class and passes in the house data
        the_house = House(house_data)

        # right now i am printing each house that we create, we could then store each 
        # house on self.houses or something
        print(the_house)

