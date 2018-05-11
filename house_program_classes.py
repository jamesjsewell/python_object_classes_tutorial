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

# creates an instance of a house and allows the user to set its attributes and create its rooms
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

        # this is a function i wrote that is imported from another file. it takes an object and list of attributes
        # to allow the user to set on the object
        let_user_update_object(the_object = self.house, attributes_list = house_attributes)

    # allows the user to define each room of the house, the rooms get stored on the house instance in an array
    def create_rooms_of_house(self):
        
        print('now enter details about the rooms of the house')

        done_adding_rooms = False

        rooms_array = []

        # will allow the user to continue adding rooms until done_adding_rooms becomes false
        while done_adding_rooms != True:
            
            # spawns a room instance
            room = Room()

            # list of attributes that the user will be asked to define
            room_attributes = [
                "room_name",
                "square_feet",
                "number_windows",
                "has_fan",
                "number_outlets",
                "floor_material",
                "number_lights"
            ]

            # i wrote this function and it lives in another file. it takes in a list 
            # of attributes that the user will be allowed to set on the room object
            # and then prompts the user to define them
            let_user_update_object(the_object = room, attributes_list = room_attributes)

            # appends the newly created room to the rooms array
            rooms_array.append(room)

            # asks the user if they want to keep adding rooms
            keep_adding_rooms = input('add another room? y/n : ')

            # the else block will escape the while loop if n is pressed by the user
            if keep_adding_rooms == 'y':

                print('\n')

            else:
                
                # escapes while loop runs the done_creating_house method
                done_adding_rooms = True
                self.done_creating_house(rooms_array)

    # takes rooms array of room objects and sets it on the house instance
    def done_creating_house(self, rooms_array):

        # sets the rooms array on the house instance
        self.house.rooms = rooms_array
        self.house.calculate_house_size()
    
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

        user_selection = int(input("1 create new house | 2 view all houses | 3 remove houses | 4 exit "))

        if user_selection == 1:

            self.add_a_new_house()

        if user_selection == 2:

            self.view_houses()

        if user_selection == 3:

            self.remove_houses()

        if user_selection == 4:

            self.exit()


    # creats a house
    def add_a_new_house(self):

        #creates an instance of the House_Builder class thereby starting that part of the app
        house_builder = House_Builder()
        self.houses.append(house_builder.house)

        #when the house_builder is complete, present the user with options again
        self.give_user_options()

    # shows all created houses
    def view_houses(self):

        print('\n')
        print('---------- houses ----------')
        print(self.houses)
        print('----------------------------')
        print('\n')

        self.give_user_options()

    # deletes houses
    def remove_houses(self):

        # when this becomes false, the user will be taken back to the main menu
        done_removing = False

        # will continue to allow the user to delete houses as long as done_removing remains false
        while done_removing == False:

            # becomes the address that the user enters
            house_to_remove = input("enter address of house to remove: ")

            # loops through houses and looks for one that matches the address the user typed in
            for a_house in self.houses:

                # checks if the adress of the house is equal to the address the user entered
                if a_house.address == house_to_remove:

                    # removes house from the houses array
                    del self.houses[self.houses.index(a_house)]

                    print(f"removed house at {house_to_remove}")

            # asks the user if they want to continue removing houses
            keep_going = input("remove more houses? y/n ")

            # the else block escapes the while loop
            if keep_going == 'y':

                print('\n')

            else:

                done_removing = True

        # brings the user back to the main menu
        self.give_user_options()

    def exit(self):

        print('goodbye')

