import requests
URL = 'https://randomuser.me/api/'
class RandomUser:
    def __init__(self):
        self.data = requests.get(URL).json()


    def get_name_title(self):
        """
        This method returns the first name
        """
        return self.data['results'][0]['name']['title']    

    def get_first_name(self):
        """
        This method returns the first name
        """
        return self.data['results'][0]['name']['first']
    
    def get_last_name(self):
        """
        This method returns the last name
        """
        return self.data['results'][0]['name']['last']

    def get_full_name(self):
        """
        This method returns the full name
        """
        return f"{self.data['results'][0]['name']['first']} {self.data['results'][0]['name']['last']}"

    def get_email(self):
        """
        This method returns the email
        """
        return self.data['results'][0]['email']

    def get_phone(self):
        """
        This method returns the phone
        """
        return self.data['results'][0]['phone'] 

    def get_cell(self):
        """
        This method returns the cell
        """
        return self.data['results'][0]['cell']

    def get_picture(self):
        """
        This method returns the picture
        """
        return self.data['results'][0]['picture']["large"]
    
    def get_gender(self):
        """
        This method returns the gender
        """
        return self.data['results'][0]['gender']
    
    def get_nationality(self):
        """
        This method returns the nationality
        """
        return self.data['results'][0]['nat']
    def get_location(self):
        """
        This method returns the location
        """
        return self.data['results'][0]['location']
    def get_street(self):
        """
        This method returns the location
        """
        return f"{self.data['results'][0]['location']["street"]["number"]} {self.data['results'][0]['location']["street"]["name"]}" 
    
    def get_country(self):
        """
        This method returns the location
        """
        return self.data['results'][0]['location']["country"]
    
    def get_state(self):
        """
        This method returns the location
        """
        return self.data['results'][0]['location']["state"]
    
    def get_city(self):
        """
        This method returns the location
        """
        return self.data['results'][0]['location']["city"]
    
    def get_postcode(self):
        """
        This method returns the location
        """
        return self.data['results'][0]['location']["postcode"]
    
    def get_date(self):
        """
        This method returns the date
        """
        return self.data['results'][0]['registered']['date']
    
    def get_dob(self):
        """
        This method returns the dob
        """
        return self.data['results'][0]['dob']

    def get_age(self):
        """
        This method returns the age
        """
        return self.data['results'][0]['dob']['age']

    def get_coordinates(self):
        """
        This method returns the age
        """
        return self.data['results'][0]["location"]['coordinates']

    def get_latitude(self):
        """
        This method returns the age
        """
        return self.data['results'][0]["location"]['coordinates']['latitude']

    def get_longtitude(self):
        """
        This method returns the age
        """
        return self.data['results'][0]["location"]['coordinates']['longitude']

    def get_timezone(self):
        """
        This method returns the age
        """
        return self.data['results'][0]["location"]['timezone']

    def get_offset(self):
        """
        This method returns the age
        """
        return self.data['results'][0]["location"]['timezone']['offset']

    def get_offset_description(self):
        """
        This method returns the age
        """
        return self.data['results'][0]["location"]['timezone']['description']