def let_user_update_object(the_object, attributes_list):

    for the_attribute in attributes_list:

        user_input = input(f"enter {the_attribute}: ")
        setattr(the_object, the_attribute, user_input)

