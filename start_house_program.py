# imports user defined house dat
# this could come from a database or user input
# i have just created some dummy data in the "house_data.py" file
import house_data 
# imorts the classes i defined in the house_program_class.py file
from house_program_classes import Neighboorhood_Program, House, Room  

# runs a method from the house_data file that returns house data
user_defined_data = house_data.get_house_data()

# passes the house data into the Neighboorhood_Program class
neighboorhood = Neighboorhood_Program(user_defined_data)

