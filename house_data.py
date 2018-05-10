def get_house_data():

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
        'guest_bath_room': {
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

    house2_rooms = {
            
        'living': {

            'room_name': 'living room',
            'square_feet': 500,
            'number_windows': 4,
            'has_fan': True,
            'number_outlets': 6,
            'floor_material': 'wood',
            'number_lights': 6
        },
        'master_bedroom': {

            'room_name': 'master bedbroom',
            'square_feet': 200,
            'number_windows': 2,
            'has_fan': True,
            'number_outlets': 6,
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
            'square_feet': 200,
            'number_windows': 2,
            'has_fan': False,
            'number_outlets': 3,
            'floor_material': 'tile',
            'number_lights': 1
        },
        'guest_bedroom': {

            'room_name': 'bedroom',
            'square_feet': 150,
            'number_windows': 1,
            'has_fan': True,
            'number_outlets': 4,
            'floor_material': 'carpet',
            'number_lights': 1

        },
        'guest_bath_room': {
            'room_name': 'guest bathroom',
            'square_feet': 140,
            'number_windows': 1,
            'has_fan': False,
            'number_outlets': 1,
            'floor_material': 'tile',
            'number_lights': 1
        },
        'kitchen': {
            'room_name': 'kitchen',
            'square_feet': 350,
            'number_windows': 3,
            'has_fan': False,
            'number_outlets': 5,
            'floor_material': 'tile',
            'number_lights': 4
        }

    }


    house3_rooms = {
            
        'living': {

            'room_name': 'living room',
            'square_feet': 300,
            'number_windows': 1,
            'has_fan': False,
            'number_outlets': 2,
            'floor_material': 'carpet',
            'number_lights': 3
        },
        'bedroom': {

            'room_name': 'bedroom',
            'square_feet': 100,
            'number_windows': 1,
            'has_fan': False,
            'number_outlets': 2,
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
            'square_feet': 100,
            'number_windows': 1,
            'has_fan': False,
            'number_outlets': 1,
            'floor_material': 'tile',
            'number_lights': 1
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

    house2 = {

        'address': '230 canal st',
        'price': '200,000',
        'color': 'blue',
        'roof_material': 'shingles',
        'has_garage': False,
        'rooms_data': house2_rooms
    }

    house3 = {

        'address': '440 canal st',
        'price': '80,000',
        'color': 'grey',
        'roof_material': 'metal',
        'has_garage': True,
        'rooms_data': house3_rooms
    }

    addresses = {
        
        '104 canal st': house1,
        '230 canal st': house2,
        '440 canal st': house3

    }

    return addresses