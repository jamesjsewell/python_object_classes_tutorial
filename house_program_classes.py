from utility_functions import let_user_update_object


# room class takes in user defined room data and stores it on itself
class Room:

    def __init__(self):
       
        self.room_name = None
        self.square_feet = None
        self.number_windows = None
        self.has_fan = None
        self.number_outlets = None
        self.floor_material = None
        self.number_lights = None
        
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
        self.create_house() 
        self.create_rooms_of_house()     
        
    def create_house(self):

        house_attributes = [
            'address',
            'price',
            'color',
            'roof_material',
            'has_garage'
        ]

        let_user_update_object(the_object = self.house, attributes_list = house_attributes)
        print(self.house)

    def create_rooms_of_house(self):
        
        print('now enter details about the rooms of the house')

        done_adding_rooms = False

        rooms_array = []

        while done_adding_rooms != True:

            room = Room()

            room_attributes = [
                "room_name",
                "square_feet",
                "number_windows",
                "has_fan",
                "number_outlets",
                "floor_material",
                "number_lights"
            ]

            let_user_update_object(the_object = room, attributes_list = room_attributes)

            rooms_array.append(room)

            keep_adding_rooms = input('add another room? y/n : ')

            if keep_adding_rooms == 'y':

                print('\n')

            else:

                done_adding_rooms = True
                self.house.rooms = rooms_array
                print(self.house)



# this class serves as the main logic container of the app
class Neighboorhood_Program:

    # this init method runs once, it's just a function that gets ran when the new instance 
    # is spawned. It takes in the house data in the addresses argument
    def __init__(self):
        
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

