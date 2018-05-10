import house_data 
from house_program_classes import Neighboorhood_Program, House, Room 
# NEIGHBORHOOD PROGRAM #
# allows user to create their own 'neighboorhood'
# and populate their 'neighboorhood' with 'houses'
# and the 'houses' are customizable 

user_defined_data = house_data.get_house_data()
neighboorhood = Neighboorhood_Program(user_defined_data)

