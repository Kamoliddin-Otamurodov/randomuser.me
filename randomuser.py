import requests
class RandomUser:
    def __init__(self , url):
        self.url = url

    def get_first_name(self):
        response = requests.get(self.url)
        data = response.json()
        return data["results"][0]["name"]["first"]

    def get_last_name(self):
        response = requests.get(self.url)
        data = response.json()
        return data["results"][0]["name"]["last"]

    def get_gender(self):
        response = requests.get(self.url)
        data = response.json()
        return data["results"][0]["gender"]

    def get_country(self):
        response = requests.get(self.url)
        data = response.json()
        return data["results"][0]["location"]["country"]

    def get_email(self):
        response = requests.get(self.url)
        data = response.json()
        return data["results"][0]["email"]