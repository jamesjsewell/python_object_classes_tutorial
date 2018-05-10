class Room:

    def __init__(self, room_data):
       
        self.room_name = room_data['room_name']
        self.square_feet = room_data['square_feet']
        self.number_windows = room_data['number_windows']
        self.has_fan = room_data['has_fan']
        self.number_outlets = room_data['number_outlets']
        self.floor_material = room_data['floor_material']
        self.number_lights = room_data['number_lights']
        

    def __repr__(self):
        return (f"\n {self.room_name} ... square feet: {self.square_feet}, windows: {self.number_windows}, has fan? {self.has_fan}, outlets: {self.number_outlets}, floor: {self.floor_material}, lights: {self.number_lights} \n")
     
class House:

    def __init__(self, house_data):

        self.address = house_data['address']
        self.price = house_data['price']
        self.rooms = []
        self.square_feet = None
        self.color = house_data['color']
        self.roof_material = house_data['roof_material']
        self.has_garage = house_data['has_garage']
        self.rooms_data = house_data['rooms_data']
        self.Room_class = Room

        self.create_rooms()
        self.calculate_house_size()

    def create_rooms(self):

        for the_room_name in self.rooms_data:

            the_room_data = self.rooms_data[the_room_name]
            the_room_object = self.Room_class(the_room_data)
            self.rooms.append(the_room_object)

    def calculate_house_size(self):

        total_square_feet = 0
        i = 0

        while i < len(self.rooms):

            the_room_obj = self.rooms[i]
            room_square_feet = the_room_obj.square_feet

            total_square_feet = total_square_feet + room_square_feet

            i += 1

        self.square_feet = total_square_feet

    def __repr__(self):

        return (f"\n address: {self.address} \n price: {self.price} \n square feet: {self.square_feet} \n color: {self.color} \n roof: {self.roof_material} \n has garage? {self.has_garage} \n rooms: {self.rooms} \n")

class Neighboorhood_Program:

    def __init__(self, addresses):
        
        self.addresses = addresses

        for address in self.addresses:
            house_data = self.addresses[address]
            self.add_a_new_house(house_data)

    def add_a_new_house(self, house_data):

        the_house = House(house_data)
        print(the_house)

    # def view_a_house(self):

    #     pass

    # def view_all_houses(self):

    #     pass

    # def delete_a_house(self):

    #     pass
    
    # def delete_all_houses(self):
    #     pass

    # def edit_house(self):
    #     pass
