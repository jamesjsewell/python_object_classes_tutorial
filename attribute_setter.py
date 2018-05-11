
# takes an object and prompts the user to define the attributes of that object that are in the attributes_list 
def let_user_update_object(the_object, attributes_list):

    # the_attribute becomes each attribute in the attributes_list
    for the_attribute in attributes_list:

        # user_input asks the user to define each attribute listed
        user_input = input(f"enter {the_attribute}: ")

        # python method for setting an attribute and it's value on an object
        setattr(the_object, the_attribute, user_input)

