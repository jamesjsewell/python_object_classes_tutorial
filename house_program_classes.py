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

# stores the houses's room objects on itself in an array. Also takes in other house data
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
            room_square_feet = int(the_room_obj.square_feet)

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
        self.houses = []
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
                self.done_creating_house(rooms_array)

    def done_creating_house(self, rooms_array):

        self.house.rooms = rooms_array
        self.house.calculate_house_size()
        self.houses.append(self.house)
        print('\n')
        print(f'house at {self.house.address} created')
        print(self.house)
        

# this class serves as the main logic container of the app
class Neighboorhood_Program:

    # this init method runs once, it's just a function that gets ran when the new instance 
    # is spawned.
    def __init__(self):

        self.houses = []
        
        # runs the user prompt
        self.give_user_options()

    #presents the user with options in the console
    def give_user_options(self):

        user_selection = int(input("1 create new house | 2 view all houses "))

        if user_selection == 1:

            self.add_a_new_house()

        if user_selection == 2:

            self.view_houses()


    # creats a house
    def add_a_new_house(self):

        #creates an instance of the House_Builder class thereby starting that part of the app
        house_builder = House_Builder()
        self.houses.append(house_builder.house)

        #when the house_builder is complete, present the user with options again
        self.give_user_options()

    def view_houses(self):

        print('\n')
        print('---------- houses ----------')
        print(self.houses)
        print('----------------------------')
        print('\n')

        self.give_user_options()

