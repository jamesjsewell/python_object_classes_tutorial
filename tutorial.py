# NEIGHBORHOOD PROGRAM #
# allows user to create their own 'neighboorhood'
# and populate their 'neighboorhood' with 'houses'
# and the 'houses' are customizable


# square feet
# number of windows
# fan/no fan
# number of outlets
# floor material
# number of lights
class Room:

    def __init__(self, room_data):
        print(room_data['room_name'])
        self.room_name = room_data['room_name']
        self.square_feet = room_data['square_feet']
        self.number_windows = room_data['number_windows']
        self.has_fan = room_data['has_fan']
        self.number_outlets = room_data['number_outlets']
        self.floor_material = room_data['floor_material']
        self.number_lights = room_data['number_lights']
        

    def __repr__(self):
        return (f"| {self.room_name} .... square feet: {self.square_feet}, windows: {self.number_windows}, has fan? {self.has_fan}, outlets: {self.number_outlets}, floor: {self.floor_material}, lights: {self.number_lights} \n")
    
    

# this is a house
# a house has rooms ( see Rooms class )
# address
# price
# a color
# roof material
# garage/no garage
# square feet
# rooms
class House:

    def __init__(self, house_data, Room_class):

        print(house_data['address'])

        self.address = house_data['address']
        self.price = house_data['price']
        self.rooms = []
        self.square_feet = None
        self.color = house_data['color']
        self.roof_material = house_data['roof_material']
        self.has_garage = house_data['has_garage']
        self.rooms_data = house_data['rooms_data']
        self.Room_class = Room_class

        self.create_rooms()
        #self.calculate_house_size()

        pass

    def calculate_house_size(self):
        #self.rooms
        #self.square_feet = result
        pass

    def create_rooms(self):


        for the_room_name in self.rooms_data:

            the_room_data = self.rooms_data[the_room_name]
            the_room_object = self.Room_class(the_room_data)
            self.rooms.append(the_room_object)

    def __repr__(self):

        return (f"\n address: {self.address} \n price: {self.price} \n square feet: {self.square_feet} \n color: {self.color} \n roof: {self.roof_material} \n has garage? {self.has_garage} \n rooms: {self.rooms} | \n")

class Neighboorhood_Program:

    def __init__(self, house_class):

        print("program started")
    
        self.house_class = house_class
        self.houses_dict = {}
        
        #dummy data from a 'user'
        house1_rooms = {
        
            'living': {

                'room_name': 'living room',
                'square_feet': 400,
                'number_windows': 2,
                'has_fan': True,
                'number_outlets': 4,
                'floor_material': 'wood',
                'number_lights': 3
            },
            'bedroom': {

                'room_name': 'bedroom',
                'square_feet': 150,
                'number_windows': 1,
                'has_fan': True,
                'number_outlets': 4,
                'floor_material': 'carpet',
                'number_lights': 1

            },
            'bath_room': {
                'room_name': 'bathroom',
                'square_feet': 100,
                'number_windows': 1,
                'has_fan': False,
                'number_outlets': 1,
                'floor_material': 'tile',
                'number_lights': 1
            },
            'kitchen': {
                'room_name': 'kitchen',
                'square_feet': 200,
                'number_windows': 1,
                'has_fan': False,
                'number_outlets': 3,
                'floor_material': 'tile',
                'number_lights': 4
            }

        }

        house1 = {

            'address': '104 canal st',
            'price': '120,000',
            'color': 'grey',
            'roof_material': 'metal',
            'has_garage': True,
            'rooms_data': house1_rooms
        }

        self.addresses = {
            
            '104 canal st': house1
        
        }

        for address in self.addresses:
            house_data = self.addresses[address]
            self.add_a_new_house(house_data)



    #address, price, rooms, color, roof_material, has_garage, room
    def add_a_new_house(self, house_data):

        the_house = House(house_data, Room)
        print(the_house)
        # self.houses_dict[house_data['address']]


    def view_a_house(self):

        pass

    def view_all_houses(self):

        pass

    def delete_a_house(self):

        pass
    
    def delete_all_houses(self):
        pass

    def edit_house(self):
        pass

neighboorhood = Neighboorhood_Program(House)

