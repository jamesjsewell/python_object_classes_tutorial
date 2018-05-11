# imports the function that will be used to enable the user to set attributes of objects
from attribute_setter import let_user_update_object

# imports the classes necessary for creating houses
from house_and_room import House, Room, House_Builder
        
# this class serves as the main logic container of the app
class Neighboorhood_Program:

    # this init method runs once, it's just a function that gets ran when the new instance 
    # is spawned.
    def __init__(self):

        # this is where the houses will be stored
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

        # creates an instance of the House_Builder class thereby starting that part of the app
        house_builder = House_Builder()

        # stores the newly created house instance in the houses array 
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

        # takes user back to home screen
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

