from randomuser import RandomUser

user = RandomUser("https://randomuser.me/api/")
 
print(type(user))
print(user.get_first_name()) 
print(user.get_last_name())
print(user.get_gender())
print(user.get_country())
print(user.get_email())