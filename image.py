import requests
from collections import namedtuple

class Search:
    def __init__(self, limit):
        self.key = "96d05359d76f4e758906539daeab939e"
        self.url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
        self.limit = limit

    def bing(self, query):
        headers = {"Ocp-Apim-Subscription-Key" : self.key}
        params  = {"q": query, "license": "public", "imageType": "photo"}
        response = requests.get(self.url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def getThumbs(self, query):
        return [img["thumbnailUrl"] for img in self.bing(query)["value"][:self.limit]]

    def getLinks(self, query):
        return [img["contentUrl"] for img in self.bing(query)["value"][:self.limit]]

    def getLinksAndThumbs(self, query):
        Image = namedtuple('Image', 'thumb, link')
        response = self.bing(query)["value"][:self.limit]
        thumbs = [img["thumbnailUrl"] for img in response]
        links = [img["contentUrl"] for img in response]
        return [Image._make([x, y]) for x, y in zip(thumbs, links)]