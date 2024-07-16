from randomuser import RandomUser
from pprint import pprint

user = RandomUser()
 
print(type(user))
print(user.get_first_name()) 
print(user.get_last_name())
print(user.get_full_name())
print(user.get_email())
print(user.get_phone())
print(user.get_cell())
print(user.get_picture())
print(user.get_gender())
print(user.get_nationality())
pprint(user.get_location())
print(user.get_street())
print(user.get_country())
print(user.get_state())
print(user.get_city())
print(user.get_postcode())
print(user.get_date())
print(user.get_dob())
print(user.get_age())