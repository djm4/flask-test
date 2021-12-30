import requests


class BPDTSTestAppAPI:

    def __init__(self, base_url=None):
        self.base_url = base_url

    def api_request(self, url=None):
        """
        Perform the API request at the provided URL
        :param url:
        :return: object parsed from the JSON response
        """
        response = requests.get(url)
        return response.json()

    def instructions(self):
        """
        API request to the /instructions endpoint
        :return: Dictionary containing the instructions
        """
        if self.base_url == 'mock':
            return {
                'todo':
                    'Build an API which calls this API, and returns people who are listed as either living in London,'
                    + ' or whose current coordinates are within 50 miles of London.'
                    + ' Push the answer to Github, and send us a link.'
            }
        else:
            return self.api_request(url=f'{self.base_url}/instructions')

    def users(self):
        """
        API request to the /users endpoint
        :return: Array of users in the database
        """
        if self.base_url == 'mock':
            return \
                [
                    {
                        "id": 1,
                        "first_name": "Maurise",
                        "last_name": "Shieldon",
                        "email": "mshieldon0@squidoo.com",
                        "ip_address": "192.57.232.111",
                        "latitude": 34.003135,
                        "longitude": -117.7228641
                    },
                    {
                        "id": 2,
                        "first_name": "Wesley",
                        "last_name": "Wyndam-Pryce",
                        "email": "watcher@angelinvestigations.com",
                        "ip_address": "156.112.56.9",
                        "latitude": 34.019074357518875,
                        "longitude": -118.18768605300842
                    },
                    {
                        "id": 3,
                        "first_name": "Bendix",
                        "last_name": "Halgarth",
                        "email": "bhalgarth1@timesonline.co.uk",
                        "ip_address": "4.185.73.82",
                        "latitude": -2.9623869,
                        "longitude": 104.7399789
                    },
                    {
                        "id": 4,
                        "first_name": "Yasmin",
                        "last_name": "Khan",
                        "email": "ykhan@hallamshire-police.gov.uk",
                        "ip_address": "50.123.56.74",
                        "latitude": "53.381160",
                        "longitude": "-1.459786"
                    },
                    {
                        "id": 5,
                        "first_name": "Nowhere",
                        "last_name": "Man",
                        "email": "man@nowhere-land.org",
                        "ip_address": "0.0.0.0"
                    },
                ]
        else:
            return self.api_request(url=f'{self.base_url}/users')

    def user(self, id=None):
        """
        API request to the /user/{id} endpoint
        :param id: the numeric ID of the user to be fetched
        :return: Dictionary representing the user
        """
        if self.base_url == 'mock' and id == 1:
            return \
                {
                  "id": 1,
                  "first_name": "Maurise",
                  "last_name": "Shieldon",
                  "email": "mshieldon0@squidoo.com",
                  "ip_address": "192.57.232.111",
                  "latitude": 34.003135,
                  "longitude": -117.7228641,
                  "city": "Kax"
                }
        else:
            return self.api_request(url=f'{self.base_url}/user/{id}')

    def city_users(self, city=None):
        """
        API request to the /city/{city}/users endpoint
        :param city: Capitalised name of the city
        :return: Array of users in that city
        """
        if self.base_url == 'mock' and city == 'Kax':
            return \
                [
                  {
                    "id": 1,
                    "first_name": "Maurise",
                    "last_name": "Shieldon",
                    "email": "mshieldon0@squidoo.com",
                    "ip_address": "192.57.232.111",
                    "latitude": 34.003135,
                    "longitude": -117.7228641
                  },
                  {
                    "id": 854,
                    "first_name": "Nelly",
                    "last_name": "Thurley",
                    "email": "nthurleynp@joomla.org",
                    "ip_address": "46.72.120.66",
                    "latitude": 34.003135,
                    "longitude": -117.7228641
                  }
                ]
        else:
            return self.api_request(url=f'{self.base_url}/city/{city}/users')
